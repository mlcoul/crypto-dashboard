# crypto_app.py
# Author: Mohamed Coulibaly
# Description: Real-time crypto dashboard with local LLM summaries

import streamlit as st
import requests
import datetime
import plotly.graph_objects as go

st.set_page_config(page_title="💰 Crypto Dashboard", layout="wide")
st.title("📍 MHD  Crypto Dashboard")

# ---------------------------
# List of available coins
# ---------------------------
AVAILABLE_COINS = ["bitcoin", "ethereum", "solana", "dogecoin", "cardano", "ripple", "litecoin"]

# ---------------------------
# Multiselect widget
# ---------------------------
selected_coins = st.multiselect("Select coins to track:", AVAILABLE_COINS, default=["bitcoin", "ethereum"])

# ---------------------------
# Fetch current prices
# ---------------------------
def get_crypto_data(coin_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(coin_ids),
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

# ---------------------------
# Fetch 2-day historical price
# ---------------------------
def get_price_history(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "2"
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        prices = data.get("prices", [])
        print(f"\n📊 DEBUG [{coin_id}]:", prices[:3])
        if not prices:
            st.warning(f"No data returned for {coin_id}")
            return [], []
        times = [datetime.datetime.fromtimestamp(p[0] / 1000) for p in prices]
        values = [p[1] for p in prices]
        return times, values
    except Exception as e:
        st.error(f"Error fetching history for {coin_id}: {e}")
        return [], []

# ---------------------
# Prices Display
# ---------------------
st.subheader("💹 Prices & 24h Change")

crypto = get_crypto_data(selected_coins)
cols = st.columns(len(crypto))

for i, (coin, data) in enumerate(crypto.items()):
    with cols[i]:
        st.metric(
            label=coin.capitalize(),
            value=f"${data['usd']:,}",
            delta=f"{data['usd_24h_change']:.2f}%",
            delta_color="normal"
        )

# ---------------------
# 24h Trend Charts
# ---------------------
st.divider()
st.subheader("📈 24-Hour Price Trends")

for coin in selected_coins:
    times, prices = get_price_history(coin)
    if times and prices:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=times, y=prices, mode='lines', name=coin.capitalize()))
        fig.update_layout(
            title=f"{coin.capitalize()} Price (Last 24h)",
            xaxis_title="Time",
            yaxis_title="Price (USD)",
            margin=dict(l=40, r=40, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)

# ---------------------
# Static News Section
# ---------------------
st.divider()
st.subheader("📰 Latest Crypto News")

from langchain_community.llms import Ollama

# LLM input
st.divider()
st.subheader("🤖 LLM Crypto Insight")
user_question = st.text_input("Ask the AI about the crypto trends above:")

if user_question:
    llm = Ollama(model="llama3")  # Or "mistral"
    response = llm.invoke(user_question)
    st.write("📌 AI Response:")
    st.markdown(response)




news = [
    {"title": "Bitcoin rises above $60k", "link": "https://www.coindesk.com"},
    {"title": "Ethereum ETF decision coming soon", "link": "https://cointelegraph.com"},
    {"title": "Crypto market volatility increases", "link": "https://decrypt.co"}
]

for item in news:
    st.markdown(f"🔗 [{item['title']}]({item['link']})")

st.caption(f"Updated at {datetime.datetime.now().strftime('%H:%M:%S')}")

