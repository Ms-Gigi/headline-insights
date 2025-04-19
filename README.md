# 📰 Headline Analyzer Project

Analyze real-world news headlines using Python — from a command-line tool to a full-featured interactive Streamlit dashboard.

---

## 🔍 Overview

This project explores and visualizes headline data through two powerful versions:

### 🧑🏽‍💻 CLI Version (Terminal-Based)
A Python-based command-line tool that lets users load `.txt` files and perform interactive analysis via a menu interface. 

### 📊 Streamlit App (Web Dashboard)
A dynamic, web-based dashboard that allows users to upload structured JSON datasets, perform real-time sentiment and word analysis, and view visual insights. 

---

## 🛠️ Features

### ✅ Shared Capabilities (Both Versions)
- Count how many headlines contain a specific word
- Analyze word frequency (top 10 most used)
- Filter headlines by length
- View longest/shortest headlines
- Search headlines using AND/OR logic
- Visualize word frequency with bar charts

### 🧑🏽‍💻 CLI-Only Features
- Fully menu-driven program with terminal prompts
- Saves analysis to report file
- Simple input/output for `.txt` headline files

### 📊 Streamlit-Only Features
- Upload `.json` datasets (default: Huffington Post dataset)
- Sentiment analysis using TextBlob (positive, negative, neutral)
- Average sentiment scores per news category
- Interactive charts and filtered word breakdowns
- Word clouds (coming soon!)

---

## 🧠 Skills Demonstrated

### 🐍 Core Python
- File I/O and error handling
- Custom functions and modular design
- Working with lists, strings, dictionaries, and `collections.Counter`

### 🧪 Data Science & NLP
- Data cleaning and tokenization
- Sentiment analysis with TextBlob
- Word frequency and category comparisons
- Exploratory Data Analysis (EDA) with Pandas and Seaborn

### 📊 Visualization
- Bar charts for sentiment and frequency
- Histogram distributions
- Interactive filtering with Streamlit UI components

## 🧪 Technologies Used

- Python 3.9+
- Streamlit
- TextBlob
- NLTK
- Pandas
- Seaborn & Matplotlib
- `collections.Counter`

