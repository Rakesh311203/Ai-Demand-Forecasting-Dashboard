import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
import google.generativeai as genai


API_KEY = 'API_KEY GOES HERE' 
genai.configure(api_key="API_KEY")

st.set_page_config(page_title='AI Demand Forecast', layout='wide')

# --- UI HEADER ---
st.title('📦 AI Demand Forecasting Dashboard')
st.markdown("### Replicates SAP IBP Logic | Project 1")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Configuration")
store = st.sidebar.selectbox('Select Store', [1, 2, 3, 4, 5])
item = st.sidebar.selectbox('Select Item', list(range(1, 11)))
lead_time = st.sidebar.slider('Lead Time (Days)', 3, 21, 7)
safety_pct = st.sidebar.slider('Safety Stock %', 10, 50, 20)

# --- DATA ENGINE ---
@st.cache_data # This prevents re-loading the CSV every time you click a button
def load_data():
    # Ensure train.csv is in a folder named 'data' relative to this script
    df = pd.read_csv('data/train.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

raw_df = load_data()
df = raw_df[(raw_df['store'] == store) & (raw_df['item'] == item)]
df = df.rename(columns={'date': 'ds', 'sales': 'y'})

# --- FORECASTING ENGINE ---
with st.spinner('Calculating Forecast...'):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)

# --- VISUALIZATION ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], name='Historical Sales', line=dict(color='teal')))
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='AI Forecast', line=dict(color='orange', dash='dash')))
fig.update_layout(title=f'Store {store} - Item {item} Forecast', height=450, template='plotly_white')
st.plotly_chart(fig, use_container_width=True)

# --- SUPPLY CHAIN KPI CALCULATIONS ---
next90 = forecast[forecast['ds'] > df['ds'].max()].head(90)
avg_d = round(next90['yhat'].mean(), 1)
ss = round(avg_d * lead_time * (safety_pct / 100))
rop = round(avg_d * lead_time + ss)

col1, col2, col3 = st.columns(3)
col1.metric('Avg Daily Forecast', f'{avg_d} units')
col2.metric('Safety Stock (Buffer)', f'{ss} units')
col3.metric('Reorder Point (ROP)', f'{rop} units')

st.divider()

# --- AI PLANNING BRIEF (GEMINI) ---
st.subheader("🤖 AI Procurement Insights")
if st.button('Generate Planning Brief'):
    with st.spinner('Gemini is analyzing supply chain risks...'):
        max_f = round(next90['yhat'].max(), 1)
        max_dt = next90.loc[next90['yhat'].idxmax(), 'ds'].strftime('%d %b %Y')
        
        prompt = f"""You are a senior Demand Planner. 
        Write a 3-paragraph procurement brief based on these stats:
        - Store: {store}, Item: {item}
        - Avg daily demand: {avg_d}
        - Peak demand: {max_f} on {max_dt}
        - Reorder point: {rop}
        
        Focus on inventory health and stockout prevention. Be professional."""

        try:
            # Using the path we verified in your notebook
            model_ai = genai.GenerativeModel('models/gemini-3.1-flash-lite-preview')
            response = model_ai.generate_content(prompt)
            st.info(response.text)
        except Exception as e:
            st.error(f"AI Service Error: {e}")
