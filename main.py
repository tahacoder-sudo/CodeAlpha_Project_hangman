# Stock Portfolio Tracker
# This program allows users to add, remove, and track stocks in their portfolio.
# It uses a dictionary to store stock data, where the key is the stock symbol and the value is a dictionary containing quantity and price.

# Defining a dictionary to store the portfolio
portfolio = {}


def add_stock(symbol, quantity, price):
    """
    Adds a stock to the portfolio.
    If the stock already exists, it updates the quantity and average price.
    """
    if symbol in portfolio:
        existing_quantity = portfolio[symbol]["quantity"]
        existing_price = portfolio[symbol]["price"]

        # Calculating new average price
        new_quantity = existing_quantity + quantity
        new_price = ((existing_quantity * existing_price) + (quantity * price)) / new_quantity

        portfolio[symbol] = {"quantity": new_quantity, "price": new_price}
    else:
        portfolio[symbol] = {"quantity": quantity, "price": price}

    print(f"Added {quantity} shares of {symbol} at ${price} each.")


def remove_stock(symbol, quantity):
    """
    Removes stocks from the portfolio.
    If the quantity to remove is greater than available, it deletes the stock.
    """
    if symbol in portfolio:
        if quantity >= portfolio[symbol]["quantity"]:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol}.")
        else:
            portfolio[symbol]["quantity"] -= quantity
            print(f"Removed {quantity} shares of {symbol}. Remaining: {portfolio[symbol]['quantity']}")
    else:
        print(f"{symbol} not found in portfolio.")


def view_portfolio():
    """
    Displays the current stock portfolio.
    """
    if not portfolio:
        print("Portfolio is empty.")
        return

    print("\nCurrent Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['quantity']} shares at ${data['price']:.2f} each")


# Example Usage
add_stock("AAPL", 10, 150)  # Adding 10 shares of Apple at $150 each
add_stock("GOOGL", 5, 2800)  # Adding 5 shares of Google at $2800 each
add_stock("AAPL", 5, 155)  # Adding more Apple shares, should update avg price
view_portfolio()  # Display portfolio
remove_stock("AAPL", 8)  # Removing some Apple shares
view_portfolio()  # Display updated portfolio
remove_stock("GOOGL", 5)  # Removing all Google shares
view_portfolio()  # Final portfolio display






























