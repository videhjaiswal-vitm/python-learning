python
import urllib.request
import json

def get_gold_price():
    # Using a free public API to fetch global commodity or currency data
    # (For learning purposes, we simulate the live price payload)
    print("Fetching live data from commodity feed...")
    
    # Let's simulate a market dip to test your Markdown rules
    live_price_usd = 4095.00 
    return live_price_usd

def analyze_market():
    baseline = 4164.90  # Target price from your monitor_gold.md
    current = get_gold_price()
    
    # Calculate percentage deviation
    percent_change = ((current - baseline) / baseline) * 100
    
    print(f"\n--- Market Report ---")
    print(f"Baseline Price: ${baseline:,.2f}")
    print(f"Current Live Price: ${current:,.2f}")
    print(f"Net Change: {percent_change:.2f}%")
    print(f"---------------------")
    
    # Triggers mapped to your markdown scenarios
    if percent_change <= -1.5:
        print("🚨 CRITICAL: Market is down. Execute [Scenario A] from monitor_gold.md!")
    elif percent_change >= 1.5:
        print("📈 CRITICAL: Market is spiking. Execute [Scenario B] from monitor_gold.md!")
    else:
        print("⚖️ STABLE: Price movement is normal. Stand by.")

if __name__ == "__main__":
    analyze_market()
