# Main script to run the arbitrage logic.

import asyncio
from arbitrage import Arbitrage

async def main():
    # Placeholder credentials
    uniswap_wss_url = "wss://mainnet.infura.io/ws/v3/a1b2c3d4e5f67890123456789abcdef0"
    kraken_api_key = "kX9mZ3pQ7rT2vW8yN6jF1hL4cB0aK5eD2uI8oP3qR7tY9"
    kraken_api_secret = "sM2nX8vC4qP9wL3tR7kF0jY6hB1aD5eG8iO4uQ2zT9mW3"

    arbitrage = Arbitrage(uniswap_wss_url, kraken_api_key, kraken_api_secret)

    while True:
        await arbitrage.check_arbitrage()
        await asyncio.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    asyncio.run(main())