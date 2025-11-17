from satish_currency_lib.currency_convertor import CurrencyConverter
from decimal import Decimal, InvalidOperation , getcontext
converter = CurrencyConverter()
#obj.main()

'''
converted_result = converter.convert_currency("EUR", "JPY", 123.45)
if isinstance(converted_result, Decimal):
    print(f"Converted amount: {converted_result}")
else:
    print(f"Invalid input: {converted_result}")

'''
converter.main()
