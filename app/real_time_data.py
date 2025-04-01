import random
import asyncio

# Simulating stock price updates
async def simulate_stock_updates():
    stock_prices = {"AAPL": 150.0, "GOOG": 2800.0, "TSLA": 700.0}
    while True:
        for ticker in stock_prices:
            stock_prices[ticker] *= random.uniform(0.98, 1.02)  # Simulating price fluctuation
        await asyncio.sleep(1)
        yield stock_prices
