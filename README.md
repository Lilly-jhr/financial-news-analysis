## Financial News Analysis Project
Overview
This project aims to analyze the impact of financial news sentiment on stock price movements. By conducting exploratory data analysis (EDA) and quantitative analysis, the project seeks to provide insights that enhance predictive analytics capabilities for financial forecasting and investment strategies.

Project Structure
bash
Copy code
financial-news-analysis/
│
├── src/
│   ├── utils.py           # Utility functions for analysis and visualization
│   ├── data_preprocessing.py  # Data preprocessing functions
│
├── notebooks/
│   ├── EDA_raw_analyst_ratings.ipynb   # EDA on raw analyst ratings data
│   ├── EDA_GOOG.ipynb      # Quantitative analysis for Google stock
│   ├── EDA_MSFT.ipynb      # Quantitative analysis for Microsoft stock
│
├── data/
│   ├── raw/
│   │   ├── raw_analyst_ratings.csv    # Raw dataset of analyst ratings
│   ├── processed/
│   │   ├── processed_analyst_ratings.csv  # Processed dataset with sentiment scores
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/financial-news-analysis.git
cd financial-news-analysis
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Exploratory Data Analysis (EDA): Open the EDA_raw_analyst_ratings.ipynb notebook to perform exploratory analysis on the raw analyst ratings data.
Quantitative Analysis: Use the respective stock analysis notebooks (EDA_GOOG.ipynb, EDA_MSFT.ipynb) to analyze stock data.
Run the Notebooks: Use Jupyter Notebook or Jupyter Lab to run the notebooks interactively.
Project Goals
Analyze the sentiment of financial news articles.
Correlate sentiment scores with stock price movements to identify trends.
Provide insights for better investment strategies.
