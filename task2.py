from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()

    print("Welcome to Currency Converter!")
    print("Supported currencies: USD, EUR, GBP, JPY, INR")

    from_currency = input("Enter the currency you want to convert from: ").upper()
    to_currency = input("Enter the currency you want to convert to: ").upper()
    amount = float(input("Enter the amount: "))

    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except:
        print("Invalid currencies or conversion not supported.")

currency_converter()
