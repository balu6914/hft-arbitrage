# Main script to run the arbitrage logic.

import asyncio
from arbitrage import Arbitrage

async def main():
    # Replace with your credentials
    uniswap_wss_url = "wss://mainnet.infura.io/ws/v3/YOUR_PROJECT_ID"
    kraken_api_key = "YOUR_KRAKEN_API_KEY"
    kraken_api_secret = "YOUR_KRAKEN_API_SECRET"

    arbitrage = Arbitrage(uniswap_wss_url, kraken_api_key, kraken_api_secret)

    while True:
        await arbitrage.check_arbitrage()
        await asyncio.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    asyncio.run(main())