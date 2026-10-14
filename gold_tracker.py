python
# Baseline price from our gold-rules.md
baseline_price = 4164.90  
current_price = 4050.00   # Suppose the price dropped today

# Calculate percentage change
price_change = ((current_price - baseline_price) / baseline_price) * 100

print(f"Current Gold Price: ${current_price}")
print(f"Price Change: {price_change:.2%}")

# Trigger marketing rule based on our .md file
if price_change <= -1.5:
    print("🚨 ALERT: Price dropped > 1.5%. Trigger Scenario A (Buy the Dip) Marketing Campaign!")
elif price_change >= 1.5:
    print("📈 ALERT: Price rose > 1.5%. Trigger Scenario B (Secure Wealth) Marketing Campaign!")
else:
    print("⚖️ Market is stable. No urgent campaign needed.")
