## Fetches ETH price from Kraken.

import asyncio
import ccxt.async_support as ccxt
import json

class KrakenPrice:
    def __init__(self, api_key, api_secret):
        self.exchange = ccxt.kraken({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True
        })

    async def get_eth_price(self):
        try:
            ticker = await self.exchange.fetch_ticker('ETH/USDC')
            price = ticker['last']
            return price
        except Exception as e:
            print(f"Kraken price fetch error: {e}")
            return None
        finally:
            await self.exchange.close()

async def main():
    # Replace with your Kraken API key and secret
    api_key = "YOUR_KRAKEN_API_KEY"
    api_secret = "YOUR_KRAKEN_API_SECRET"
    kraken = KrakenPrice(api_key, api_secret)
    price = await kraken.get_eth_price()
    print(f"Kraken ETH Price: ${price:.2f}")

if __name__ == "__main__":
    asyncio.run(main())