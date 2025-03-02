import yfinance as yf  # For fetching stock data
import pandas as pd    # For data manipulation and display

def get_stock_data(ticker, period="1y"):  # Default period is 1 year
    """Fetches historical stock data from yfinance."""
    try:
        data = yf.download(ticker, period=period)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def display_portfolio(portfolio):
    """Displays the current portfolio in a formatted way."""

    if not portfolio:
        print("Your portfolio is empty.")
        return

    df = pd.DataFrame.from_dict(portfolio, orient='index')
    print(df)


def add_stock(portfolio, ticker, quantity):

    data = get_stock_data(ticker)
    if data is None:
        return portfolio  # Return the portfolio unchanged if data fetch fails

    current_price = data['Close'][-1]  # Get the most recent closing price

    if ticker in portfolio:
        portfolio[ticker]['quantity'] += quantity
    else:
        portfolio[ticker] = {'quantity': quantity, 'purchase_price': current_price}

    print(f"Added {quantity} shares of {ticker} to your portfolio.")
    return portfolio

def remove_stock(portfolio, ticker, quantity):
    if ticker not in portfolio:
        print(f"You don't have {ticker} in your portfolio.")
        return portfolio

    if quantity >= portfolio[ticker]['quantity']:
        del portfolio[ticker]
        print(f"Removed all shares of {ticker} from your portfolio.")
    else:
        portfolio[ticker]['quantity'] -= quantity
        print(f"Removed {quantity} shares of {ticker} from your portfolio.")
    return portfolio

def calculate_portfolio_value(portfolio):
    total_value = 0
    for ticker, holdings in portfolio.items():
        data = get_stock_data(ticker)
        if data is None:  # Handle cases where data fetch fails
            print(f"Could not retrieve current price for {ticker}. Skipping in portfolio value calculation.")
            continue

        current_price = data['Close'][-1]
        total_value += holdings['quantity'] * current_price
    return total_value

def main():
    portfolio = {}  # Initialize an empty portfolio

    while True:
        print("\nStock Portfolio Tracker Menu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Calculate Portfolio Value")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()
            quantity = int(input("Enter the quantity to buy: "))
            portfolio = add_stock(portfolio, ticker, quantity)

        elif choice == '2':
            ticker = input("Enter the stock ticker to remove: ").upper()
            quantity = int(input("Enter the quantity to sell: "))
            portfolio = remove_stock(portfolio, ticker, quantity)

        elif choice == '3':
            display_portfolio(portfolio)

        elif choice == '4':
            total_value = calculate_portfolio_value(portfolio)
            print(f"Your total portfolio value is: ${total_value:.2f}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()