import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("📈 Real-Time Stock Price Tracker")

# User Input for Stock Symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, GOOGL)", "AAPL")

# Fetch Stock Data Function
def get_stock_price(stock_symbol, period="7d", interval="1h"):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period=period, interval=interval)
    return stock_data

# Fetch Data
if stock_symbol:
    stock_data = get_stock_price(stock_symbol)

    if not stock_data.empty:
        # Display Latest Stock Price
        latest_price = stock_data["Close"].iloc[-1]
        st.subheader(f"📊 Latest Stock Price of {stock_symbol}: **{latest_price:.2f} USD**")

        # Display Data Table
        st.write("### 🔍 Stock Price Data (Last 7 Days)")
        st.dataframe(stock_data.tail())

        # Plot Stock Price Graph
        st.write("### 📉 Stock Price Trend")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(stock_data.index, stock_data["Close"], label="Closing Price", color="blue")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        ax.set_title(f"Stock Price of {stock_symbol} Over Time")
        ax.legend()
        ax.grid()
        st.pyplot(fig)

    else:
        st.error("⚠️ Invalid stock symbol or no data available!")

# Footer
st.markdown("💡 **Tip:** Try stock symbols like `AAPL`, `TSLA`, `GOOGL`, `MSFT`")
