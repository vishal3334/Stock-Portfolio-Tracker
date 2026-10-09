"""
CodeAlpha Task 2: Stock Portfolio Tracker
User enters stock names and quantity. Prices come from a hardcoded dictionary.
Shows total investment and can save the result to a .txt file.
"""
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125,
}


def get_portfolio():
    portfolio = {}
    print("Available stocks and prices:")
    for name, price in STOCK_PRICES.items():
        print(f"  {name}: ${price}")
    print("\nEnter stock name and quantity. Type 'done' to finish.\n")

    while True:
        name = input("Stock name: ").upper().strip()
        if name == "DONE":
            break
        if name not in STOCK_PRICES:
            print("Stock not found. Please choose from the list above.\n")
            continue
        try:
            qty = int(input("Quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid positive number.\n")
            continue
        portfolio[name] = portfolio.get(name, 0) + qty
        print(f"Added {qty} x {name}\n")
    return portfolio


def build_report(portfolio):
    lines = ["STOCK PORTFOLIO REPORT",
             f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
             "-" * 44,
             f"{'Stock':<8}{'Qty':>6}{'Price':>10}{'Value':>14}",
             "-" * 44]
    total = 0
    for name, qty in portfolio.items():
        price = STOCK_PRICES[name]
        value = qty * price
        total += value
        lines.append(f"{name:<8}{qty:>6}{price:>10}{value:>14,.2f}")
    lines += ["-" * 44, f"{'TOTAL INVESTMENT:':<24}${total:>18,.2f}"]
    return "\n".join(lines)


def main():
    print("=== STOCK PORTFOLIO TRACKER ===\n")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    report = build_report(portfolio)
    print("\n" + report)

    save = input("\nSave result to file? (y/n): ").lower().strip()
    if save == "y":
        with open("portfolio_report.txt", "w") as f:
            f.write(report)
        print("Saved to portfolio_report.txt")


if __name__ == "__main__":
    main()
