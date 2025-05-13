# Fetches ETH price from Uniswap.

import asyncio
from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

# Uniswap V3 Pool ABI (simplified for price fetching)
UNISWAP_V3_POOL_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "slot0",
        "outputs": [
            {"name": "sqrtPriceX96", "type": "uint160"},
            {"name": "", "type": "int24"},
            {"name": "", "type": "uint16"},
            {"name": "", "type": "uint16"},
            {"name": "", "type": "uint8"},
            {"name": "", "type": "bool"},
            {"name": "", "type": "uint160"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

class UniswapPrice:
    def __init__(self, wss_url):
        self.w3 = Web3(Web3.WebsocketProvider(wss_url))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        # Uniswap V3 ETH/USDC pool address (0.05% fee)
        self.pool_address = "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640"
        self.contract = self.w3.eth.contract(address=self.pool_address, abi=UNISWAP_V3_POOL_ABI)

    async def get_eth_price(self):
        try:
            slot0 = self.contract.functions.slot0().call()
            sqrt_price_x96 = slot0[0]
            # Convert sqrtPriceX96 to price (ETH/USDC)
            price = (sqrt_price_x96 ** 2) / (2 ** 192) * 10 ** 12  # Adjust for decimals
            eth_price = 1 / price  # Convert to USDC/ETH
            return eth_price
        except Exception as e:
            print(f"Uniswap price fetch error: {e}")
            return None

async def main():
    # Placeholder Infura WebSocket URL
    wss_url = "wss://mainnet.infura.io/ws/v3/a1b2c3d4e5f67890123456789abcdef0"
    uniswap = UniswapPrice(wss_url)
    price = await uniswap.get_eth_price()
    print(f"Uniswap ETH Price: ${price:.2f}")

if __name__ == "__main__":
    asyncio.run(main())