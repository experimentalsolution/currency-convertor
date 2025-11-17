# Currency Conversion Library

A Python library for performing currency conversion between different currency types using provided currency rates and cross matrix.

## Installation

To install the library, you can use `pip`:

```bash
pip install pathto/currency-convertor-tool/satish_currency_lib/dist/satish_currency_lib-0.1.0-py2-none-any.whl

```

## Usage (how to use)

```python
from satish_currency_lib.currency_convertor import CurrencyConverter
from decimal import Decimal, InvalidOperation , getcontext

# Create an instance of CurrencyConverter

converter = CurrencyConverter()

```
## Example Usage

We need to pass from_currenncy to_currency and amount 
if matrix is defined for the currencies it will convert the currency otherwise it might give invalid input

```python
from_currency = "EUR"
to_currency = "JPY"
currency_amount = 123.45
converted_result = converter.convert_currency("EUR", "JPY", 123.45)
if isinstance(converted_result, Decimal):
    print(f"Converted amount: {converted_result}")
else:
    print(f"Invalid input: {converted_result}")
```

It also has a main method which is a user friendly interactive interface and can be implemented  like below .
```python

from satish_currency_lib.currency_convertor import CurrencyConverter
from decimal import Decimal, InvalidOperation , getcontext
converter = CurrencyConverter()
converter.main()

```
the interaction will look like below

```bash
From: AUD
Amount 234.5
To: AUD
Converted amount is: 234.50
Do you want to continue?yes
From: AUD
Amount 456.56
To: USD
Converted amount is: 382.19
Do you want to continue?yes
From: AUD
Amount 456.67
To: INR
```

**Features**

- Convert currency between different types using predefined currency rates.
- Handle cross conversions using a matrix.
- Check validity of input currency and amount.
- Precision control for converted amounts.



**API Documentation**
### `convert_currency(from_currency, to_currency, currency_amount)`

Converts currency from one type to another.

- `from_currency` (str): The currency to convert from.
- `to_currency` (str): The currency to convert to.
- `currency_amount` (float or str): The amount to convert.

Returns the converted amount if valid, or an error message.

### `check_valid_input(from_currency, to_currency, currency_amount)`

Checks if the input is valid for conversion.

- `from_currency` (str): The currency to convert from.
- `to_currency` (str): The currency to convert to.
- `currency_amount` (float or str): The amount to convert.

Returns a tuple containing a boolean indicating validity and an error message (if any).

### `main()`

A user-friendly interactive interface to perform currency conversion.

.

### `License`
This project is licensed under the MIT License - see the LICENSE file for details.