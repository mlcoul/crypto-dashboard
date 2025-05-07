# 📈 Crypto Dashboard with Real-Time LLM Insights

A customizable Streamlit web app to track real-time cryptocurrency prices and trends — enhanced with local AI (Ollama) to generate natural-language insights.

---

## 🚀 Features

- 🔄 Live prices for selected cryptocurrencies (Bitcoin, Ethereum, Solana, etc.)
- 📉 24-hour price charts (based on hourly data)
- 🧠 Ask questions like “What does Bitcoin’s trend look like?” and get LLM-powered answers
- 🔽 Multiselect dropdown to track only the coins you care about
- 💬 Local LLM integration (via [Ollama](https://ollama.com/)) for private, offline AI summaries
- 📰 Placeholder section for crypto news

---

## 📦 Tech Stack

- **[Streamlit](https://streamlit.io/)** — Interactive dashboard
- **[CoinGecko API](https://www.coingecko.com/en/api)** — Price and market data
- **[Ollama](https://ollama.com/)** — Run LLaMA3 or Mistral locally
- **LangChain** — LLM integration layer
- **Plotly** — For interactive charts

---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mlcoul/crypto-dashboard.git
cd crypto-dashboard
