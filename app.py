import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from collections import Counter
import string
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# --- Functions ---
stop_words = set(stopwords.words('english'))

def clean_and_tokenize(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return [word for word in words if word not in stop_words]

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def label_sentiment(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

# --- Streamlit App ---
st.set_page_config(page_title="Headline Insights", layout="wide")
st.title("📰 Headline Insights Dashboard")
st.markdown("Explore sentiment and word patterns across real news headlines.")

# --- File Upload ---
st.sidebar.markdown("### 📂 Upload Your Headline Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a JSON file", type=["json"])

if uploaded_file is not None:
    df = pd.read_json(uploaded_file, lines=True)
    st.success("✅ File uploaded and loaded!")
else:
    df = pd.read_json("data/News_Category_Dataset_v3.json", lines=True)
    st.info("Using default Huffington Post dataset.")

# --- Preprocessing ---
df['sentiment'] = df['headline'].apply(get_sentiment)
df['sentiment_label'] = df['sentiment'].apply(label_sentiment)
df['word_count'] = df['headline'].apply(lambda x: len(x.split()))
df['clean_tokens'] = df['headline'].apply(clean_and_tokenize)

# --- Data Preview ---
st.subheader("📋 Sample of the Data")
st.dataframe(df[['headline', 'category', 'sentiment_label']].head())

# --- Sidebar Filter ---
top_categories = df['category'].value_counts().head(10).index
category = st.sidebar.selectbox("Choose a Category", top_categories)

# --- Sentiment Distribution ---
st.subheader("🎭 Sentiment Distribution")
sentiment_counts = df['sentiment_label'].value_counts()
st.bar_chart(sentiment_counts)

# --- Average Sentiment ---
st.subheader("📊 Top Categories by Average Sentiment")
avg_sentiment = df.groupby('category')['sentiment'].mean().sort_values(ascending=False).head(10)
st.bar_chart(avg_sentiment)

# --- Top Words by Category ---
st.subheader(f"🔤 Top Words in '{category}' Headlines")
category_words = df[df['category'] == category]['clean_tokens'].explode()
top_words = pd.DataFrame(Counter(category_words).most_common(10), columns=['word', 'count'])
st.dataframe(top_words)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ by Oreoluwa | Powered by Streamlit, TextBlob, and Python")

