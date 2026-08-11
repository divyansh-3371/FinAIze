# 💰 FinAIze

### AI-Powered Financial Analysis & Investment Intelligence Platform

FinAIze is an AI-powered financial literacy and investment analysis platform designed to help users understand companies, analyze financial performance, track market sentiment, and make data-driven investment decisions.

The platform combines **financial data, fundamental analysis, stock market sentiment, document processing, and Generative AI** into a single interactive dashboard.

---

## 🚀 Features

### 📊 Investor Dashboard

Provides investors with an overview of important financial and market information.

* Stock price tracking
* Historical market data
* Financial performance visualization
* Market trend analysis
* Company-level insights
* Interactive charts and dashboards

### 🏢 Company Analysis

Analyze the financial health and performance of a company using important financial ratios.

* Profitability analysis
* Liquidity analysis
* Solvency analysis
* Efficiency ratios
* Year-over-year trend analysis
* Ratio benchmarking
* Company performance comparison

### 🧠 AI-Powered Financial Insights

FinAIze uses Generative AI to convert financial data into easy-to-understand insights.

The AI layer can help users:

* Understand financial metrics
* Summarize company performance
* Explain financial ratios
* Identify important trends
* Generate investment-related insights
* Provide financial-literacy explanations

> **Note:** AI-generated insights are for educational and informational purposes and should not be considered financial advice.

### 📈 Reddit Stock Sentiment Analysis

FinAIze analyzes discussions from Reddit to understand public sentiment toward companies and stocks.

Users can:

* Search for a company or brand
* Collect Reddit posts
* Analyze positive, negative, and neutral sentiment
* Filter posts by date
* Select different post categories
* Identify frequently discussed topics
* View highly discussed posts
* Generate AI-based summaries of public opinion

### 🤖 NLP-Based Sentiment Analysis

The project uses Natural Language Processing to classify user-generated content.

The pipeline includes:

* Text cleaning
* Emoji processing
* Stopword removal
* Lemmatization
* Text normalization
* Sentiment classification
* Transformer-based NLP models

### 📄 Financial Document Processing

FinAIze can extract information from financial documents and reports.

Supported functionality includes:

* PDF text extraction
* OCR-based text extraction
* Financial information parsing
* Automated document analysis
* AI-assisted interpretation

### 🔍 Financial Ratio Benchmarking

Financial ratios can be analyzed and compared to understand the relative performance of a company.

Examples include:

* Current Ratio
* Quick Ratio
* Debt-to-Equity Ratio
* Return on Equity
* Return on Assets
* Net Profit Margin
* Operating Margin
* Asset Turnover

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Streamlit Frontend │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ Stock Data  │  │   Reddit    │  │ Documents   │
       │    APIs     │  │   Scraper   │  │ PDF / OCR   │
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              ▼                ▼                ▼
       ┌─────────────────────────────────────────────┐
       │          Data Processing Layer              │
       │     Pandas • NLP • Financial Analysis      │
       └──────────────────────┬──────────────────────┘
                              │
                              ▼
                  ┌─────────────────────────┐
                  │    ML / NLP Models      │
                  │ Sentiment Classification│
                  └────────────┬────────────┘
                               │
                               ▼
                  ┌─────────────────────────┐
                  │      Generative AI      │
                  │ Insights & Summaries    │
                  └────────────┬────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Interactive Results │
                    │ Charts • Reports    │
                    │ Insights • Trends   │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend & Application

* **Python**
* **Streamlit**
* **Pandas**
* **Plotly**
* **Matplotlib**

### Machine Learning & NLP

* **PyTorch**
* **Hugging Face Transformers**
* **Hugging Face Datasets**
* **NLTK**
* **BERT / Transformer-based models**

### Generative AI

* **Google Gemini / Generative AI**
* AI-powered financial explanations
* Automated summaries
* Financial insight generation

### Financial Data

* **Yahoo Finance**
* **Alpha Vantage**

### Reddit & Social Media Analysis

* **PRAW**
* Reddit API
* NLP-based sentiment analysis

### Document Processing

* **Tesseract OCR**
* **pdfplumber**
* PDF text extraction
* OCR-based extraction

### Visualization

* **Plotly**
* **Matplotlib**
* **WordCloud**
* Streamlit interactive components

---

## 📂 Project Structure

```text
FinAIze/
│
├── assets/
│   ├── logo.png
│   └── ...
│
├── pages/
│   ├── investor.py
│   ├── company.py
│   └── ...
│
├── models/
│   └── ...
│
├── utils/
│   └── ...
│
├── login.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact structure may vary depending on the current development version of the project.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/divyansh-3371/FinAIze.git
cd FinAIze
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root and add the required API credentials.

```env
ALPHA_VANTAGE_API_KEY=your_api_key
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
GOOGLE_API_KEY=your_google_api_key
```

Do **not** commit API keys or other secrets to GitHub.

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will start locally and can be accessed through the URL displayed in the terminal.

---

## 📊 Example Workflow

```text
1. User selects a company
        ↓
2. FinAIze collects financial & market data
        ↓
3. Financial metrics are calculated
        ↓
4. Reddit discussions are collected
        ↓
5. NLP pipeline processes the discussions
        ↓
6. Sentiment is classified
        ↓
7. Trends and important topics are identified
        ↓
8. Generative AI produces a summary
        ↓
9. Results are displayed through interactive dashboards
```

---

## 🧪 Machine Learning Pipeline

The sentiment-analysis pipeline follows a series of preprocessing and classification steps:

```text
Reddit Posts
     │
     ▼
Text Cleaning
     │
     ▼
Emoji & Special Character Processing
     │
     ▼
Stopword Removal
     │
     ▼
Lemmatization
     │
     ▼
Tokenization
     │
     ▼
Transformer Model
     │
     ▼
Sentiment Classification
     │
     ▼
Positive / Neutral / Negative
```

---

## 💡 Key Use Cases

FinAIze can be used for:

* 📚 Financial education
* 📈 Stock market research
* 🏢 Company fundamental analysis
* 📊 Financial ratio analysis
* 🧠 Public sentiment analysis
* 🔎 Reddit-based market research
* 📄 Financial report analysis
* 🤖 AI-assisted financial insights

---

## 🔮 Future Improvements

Potential future enhancements include:

* [ ] Real-time stock monitoring
* [ ] Portfolio tracking
* [ ] Personalized investment dashboards
* [ ] Advanced financial forecasting
* [ ] Multi-source sentiment analysis
* [ ] News sentiment integration
* [ ] More advanced LLM-based financial agents
* [ ] Automated financial report generation
* [ ] User portfolio risk analysis
* [ ] Historical sentiment vs. stock-price correlation
* [ ] Improved multilingual sentiment analysis
* [ ] Cloud deployment
* [ ] Redis-based caching and performance optimization

---

## 🔐 Security

API credentials should always be stored using environment variables or a secure secrets manager.

Never upload:

```text
.env
API keys
Client secrets
Authentication tokens
Private credentials
```

to a public repository.

---

## ⚠️ Disclaimer

FinAIze is an educational and analytical software project.

The information and AI-generated insights provided by this application are intended for **educational and informational purposes only**. They should not be interpreted as professional financial, investment, tax, or legal advice.

Users should conduct their own research and consult qualified financial professionals before making investment decisions.

---

## 👨‍💻 Author

**Divyansh Bansal**

GitHub: [@divyansh-3371](https://github.com/divyansh-3371)

---

## ⭐ Support

If you find FinAIze useful or interesting, consider giving the repository a ⭐ on GitHub.

**Repository:** https://github.com/divyansh-3371/FinAIze
