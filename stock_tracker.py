stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOGLE": 150
}

stock_name = input("Enter Stock Name: ").upper()

quantity = int(input("Enter Quantity: "))

if stock_name in stocks:
    total = stocks[stock_name] * quantity

    print("\nStock Name:", stock_name)
    print("Price:", stocks[stock_name])
    print("Quantity:", quantity)
    print("Total Investment:", total)

    choice = input("\nDo you want to save the result? (yes/no): ").lower()

    if choice == "yes":
        file = open("portfolio.txt", "w")
        file.write("Stock Portfolio Details\n")
        file.write("-----------------------\n")
        file.write("Stock Name: " + stock_name + "\n")
        file.write("Price: " + str(stocks[stock_name]) + "\n")
        file.write("Quantity: " + str(quantity) + "\n")
        file.write("Total Investment: " + str(total))
        file.close()

        print("Portfolio saved successfully.")

    else:
        print("Portfolio not saved.")

else:
    print("Stock not found.")