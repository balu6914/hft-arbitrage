# Detects arbitrage opportunities and simulates trades.
from uniswap_price import UniswapPrice
from kraken_price import KrakenPrice

class Arbitrage:
    def __init__(self, uniswap_wss_url, kraken_api_key, kraken_api_secret):
        self.uniswap = UniswapPrice(uniswap_wss_url)
        self.kraken = KrakenPrice(kraken_api_key, kraken_api_secret)
        self.trade_amount = 100  # 100 ETH per trade
        self.uniswap_fee = 0.0005  # 0.05% Uniswap fee
        self.kraken_fee = 0.0016  # 0.16% Kraken maker fee

    async def check_arbitrage(self):
        uniswap_price = await self.uniswap.get_eth_price()
        kraken_price = await self.kraken.get_eth_price()

        if uniswap_price is None or kraken_price is None:
            print("Price fetch failed, skipping arbitrage check.")
            return

        # Check if buying on Uniswap and selling on Kraken is profitable
        if uniswap_price < kraken_price:
            buy_price = uniswap_price
            sell_price = kraken_price
            buy_cost = buy_price * self.trade_amount * (1 + self.uniswap_fee)
            sell_revenue = sell_price * self.trade_amount * (1 - self.kraken_fee)
            profit = sell_revenue - buy_cost

            if profit > 0:
                print(f"Arbitrage Opportunity Detected!")
                print(f"Buy {self.trade_amount} ETH on Uniswap at ${buy_price:.2f}")
                print(f"Sell {self.trade_amount} ETH on Kraken at ${sell_price:.2f}")
                print(f"Profit: ${profit:.2f}")
            else:
                print("No profitable arbitrage opportunity.")
        else:
            print("No arbitrage opportunity (Uniswap price >= Kraken price).")