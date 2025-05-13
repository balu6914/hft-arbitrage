# High-Frequency Trading (HFT) Arbitrage Proof-of-Concept

## Overview
This project demonstrates a High-Frequency Trading (HFT) system for cryptocurrency arbitrage. It monitors Ethereum (ETH) prices on Uniswap (DEX) and Kraken (CEX), detects arbitrage opportunities (e.g., buy at $1,900 on Uniswap, sell at $1,950 on Kraken), and simulates trades to calculate profits after fees.

## Tech Stack
- **Python 3.10**: Core programming language.
- **Web3.py**: For Uniswap price fetching.
- **ccxt**: For Kraken price fetching.
- **WebSocket**: For real-time data via Infura/Alchemy and Kraken.
- **Environment**: WSL Ubuntu 22.04.5, VSCode.

## Setup Instructions
1. Clone the project and navigate to the directory.
2. Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`.
3. Install dependencies: `pip install web3 ccxt websocket-client requests`.
4. Update `main.py` with your Infura/Alchemy WebSocket URL and Kraken API credentials.
5. Run the script: `python3 main.py`.

## Features
- Fetches real-time ETH/USDC prices from Uniswap and Kraken.
- Detects arbitrage opportunities and calculates profits after fees (Uniswap 0.05%, Kraken 0.16%).
- Logs trade details for demonstration purposes.

## Limitations
- Simulates trades without executing real transactions.
- Assumes constant trade amount (100 ETH) for simplicity.
- Requires stable internet and valid API credentials.

## Future Improvements
- Add real trade execution with wallet integration.
- Support multiple trading pairs and exchanges.
- Optimize latency using co-location or faster node providers.
