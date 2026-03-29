<h1> AI-Driven Demand Forecasting Dashboard </h1>

<p1> 📊 Replicating SAP IBP/APO Logic with Machine Learning
This project is a high-performance forecasting tool designed to automate inventory replenishment decisions. It combines historical sales data analysis with Meta Prophet for time-series forecasting and Google Gemini 3.1 for generating human-readable procurement briefs.

🚀 Features
* Time-Series Forecasting: Uses Prophet to handle complex seasonality, holidays, and growth trends.

* Dynamic Inventory Logic: Calculates Safety Stock and Reorder Points (ROP) based on real-time user inputs (Lead Time & Buffer %).

* AI Planning Narratives: Integrates Gemini 3.1 Flash Lite to translate raw statistical data into actionable executive summaries.

* Interactive Visualization: Built with Plotly to allow planners to hover, zoom, and analyze specific sales periods. </p1>

🛠️ Tech Stack
* Language: Python 3.12

* Forecasting: Meta Prophet

* LLM Integration: Gemini 3.1 Flash Lite

* Data Manipulation: Pandas

* Dashboard Framework: Streamlit

* Charts: Plotly

* Version Control: GitHub

📦 Installation & Setup
To run this project locally, follow these steps:

Clone the repository:
Bash
<code>git clone https://github.com/Rakesh311203/Ai-Demand-Forecasting-Dashboard.git</code> <br>
<code>cd Ai-Demand-Forecasting-Dashboard</code>

Install dependencies:
Bash
<code>pip install pandas prophet streamlit plotly google-generativeai</code>

Set up your API Key:
* Obtain a Gemini API key from Google AI Studio.
* Create a .env file or set your environment variable:

Bash
<code>export GEMINI_API_KEY='your_key_here'</code>
Run the App:
Bash
<code>streamlit run app.py</code>


<img width="1408" height="768" alt="Gemini_Generated_Image_ejpjtaejpjtaejpj" src="https://github.com/user-attachments/assets/f3a007ae-362c-447e-a99d-69436dba5a36" />
