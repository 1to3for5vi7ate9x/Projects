import requests
import time
from datetime import datetime

def get_binance_price(pair="FILUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

def get_binance_fees():
    # Example of fixed fees; you should replace with real API calls if available
    trading_fee = 0.001  # 0.1%
    withdrawal_fee = 0.01  # Example fixed fee in FIL or USD equivalent
    return trading_fee, withdrawal_fee

def calculate_arbitrage_profit(P_buy, P_sell, Q, F_buy, F_sell, F_withdraw, F_network, S=1.0):
    # Revenue from selling after fees and slippage
    revenue = P_sell * Q * (1 - F_sell) * S
    
    # Cost of buying after fees
    cost = P_buy * Q * (1 + F_buy)
    
    # Net profit calculation
    net_profit = revenue - cost - F_withdraw - F_network
    return net_profit

def monitor_arbitrage():
    # Define pair and quantity to trade
    pair = "FILUSDT"
    quantity = 10000  # Example quantity
    
    # Get prices from different exchanges
    price_binance = get_binance_price(pair)
    price_coinbase = get_binance_price(pair)  # Replace with Coinbase function
    
    # Get fees for both exchanges
    F_buy, F_withdraw = get_binance_fees()
    F_sell, F_network = get_binance_fees()  # Replace with Coinbase function
    
    # Calculate slippage adjustment factor (if needed)
    slippage_factor = 0.995  # Assuming a 0.5% slippage
    
    # Calculate net profit
    NP = calculate_arbitrage_profit(price_binance, price_coinbase, quantity, F_buy, F_sell, F_withdraw, F_network, slippage_factor)
    
    # Log results
    if NP > 0:
        print(f"Profitable arbitrage opportunity detected! Net Profit: ${NP:.2f}")
        print(f"Timestamp: {datetime.now()} | Binance Buy: ${price_binance} | Coinbase Sell: ${price_coinbase}")
    else:
        print(f"No profitable arbitrage found at {datetime.now()}")

def run_bot():
    while True:
        monitor_arbitrage()
        time.sleep(60)  # Wait 1 minute between checks (adjust as needed)

if __name__ == "__main__":
    run_bot()

