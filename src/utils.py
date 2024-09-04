import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import talib
import gensim
from gensim import corpora
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def load_data(file_path):
    return pd.read_csv(file_path)

def describe_data(df):
    return df.describe()

def plot_time_series(df, date_col, value_col, title):
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[value_col], label=value_col)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(value_col)
    plt.legend()
    plt.show()

def plot_distribution(df, col_name):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col_name], bins=30, kde=True)
    plt.title(f'Distribution of {col_name}')
    plt.xlabel(col_name)
    plt.ylabel('Frequency')
    plt.show()

def count_publications(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col])
    publication_counts = df[date_col].dt.to_period('M').value_counts().sort_index()
    publication_counts.plot(kind='bar', figsize=(14, 6))
    plt.title('Publications Per Month')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.show()


def plot_headline_length_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['headline_length'], bins=30, kde=True)
    plt.title('Distribution of Headline Lengths')
    plt.xlabel('Headline Length')
    plt.ylabel('Frequency')
    plt.show()


def plot_articles_per_publisher(df, top_n):
    publisher_counts = df['publisher'].value_counts().head(top_n)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x=publisher_counts.values, y=publisher_counts.index, palette='viridis')
    plt.title(f'Top {top_n} Publishers by Number of Articles')
    plt.xlabel('Number of Articles')
    plt.ylabel('Publisher')
    plt.show()

def plot_publication_trends(publication_trends):
    plt.figure(figsize=(14, 7))
    publication_trends.plot(kind='line')
    plt.title('Publication Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.show()


def plot_sentiment_distribution(df):
    sentiment_counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='coolwarm')
    plt.title('Sentiment Distribution of Headlines')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Headlines')
    plt.show()


def plot_sentiment_scores_by_ticker_and_month(df):
    df['date'] = pd.to_datetime(df['date'])

    df['year_month'] = df['date'].dt.to_period('M')
    sentiment_summary = df.groupby(['ticker', 'year_month'])['sentiment_score'].mean().reset_index()

    sentiment_summary['year_month'] = sentiment_summary['year_month'].dt.to_timestamp()

    plt.figure(figsize=(20, 10)) 
    sns.lineplot(x='year_month', y='sentiment_score', hue='ticker', data=sentiment_summary, marker='o')
    plt.title('Average Sentiment Score by Ticker and Month')
    plt.xlabel('Month')
    plt.ylabel('Average Sentiment Score')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(title='Ticker')
    plt.tight_layout()  
    plt.show()



def categorize_sentiment(score):
    if score > 0.2:
        return 'Highly Positive'
    elif score > 0.05:
        return 'Positive'
    elif score < -0.2:
        return 'Highly Negative'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'
    


def plot_sma(df, timeperiod):
    df['SMA'] = talib.SMA(df['Close'], timeperiod=timeperiod)

    plt.figure(figsize=(14, 8))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.plot(df['SMA'], label=f'SMA {timeperiod}', color='orange')
    plt.title(f'Stock Close Price with {timeperiod}-Period SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()


def plot_rsi(df, timeperiod):
    df['RSI'] = talib.RSI(df['Close'], timeperiod=timeperiod)

    plt.figure(figsize=(14, 4))
    plt.plot(df['RSI'], label=f'RSI {timeperiod}', color='red')
    plt.axhline(70, color='gray', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='gray', linestyle='--',  label='Oversold (30)')
    plt.title(f'Relative Strength Index (RSI) {timeperiod}-Period')
    plt.xlabel('Date')
    plt.ylabel('RSI Value')
    plt.legend()
    plt.show()



def plot_macd(df, fastperiod, slowperiod, signalperiod):
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
        df['Close'], 
        fastperiod=fastperiod, 
        slowperiod=slowperiod, 
        signalperiod=signalperiod
    )

    plt.figure(figsize=(14, 8))

    plt.subplot(2, 1, 1)
    plt.plot(df['MACD'], label='MACD', color='blue')
    plt.plot(df['MACD_signal'], label='MACD Signal', color='orange')
    plt.title('MACD and MACD Signal')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.bar(df.index, df['MACD_hist'], label='MACD Histogram', color='gray')
    plt.title('MACD Histogram')
    plt.xlabel('Date')
    plt.ylabel('Histogram')
    plt.legend()

    plt.tight_layout()
    plt.show()



