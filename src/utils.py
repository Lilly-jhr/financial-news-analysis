import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def describe_data(df):
    """Return descriptive statistics of the DataFrame."""
    return df.describe()

def plot_time_series(df, date_col, value_col, title):
    """Plot a time series graph."""
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_col], df[value_col], label=value_col)
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel(value_col)
    plt.legend()
    plt.show()

def plot_distribution(df, col_name):
    """Plot the distribution of a given column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col_name], bins=30, kde=True)
    plt.title(f'Distribution of {col_name}')
    plt.xlabel(col_name)
    plt.ylabel('Frequency')
    plt.show()

def count_publications(df, date_col):
    """Count publications per month and plot."""
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


def plot_articles_per_publisher(df):
    publisher_counts = df['publisher'].value_counts()
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x=publisher_counts.values, y=publisher_counts.index, palette='viridis')
    plt.title('Number of Articles per Publisher')
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