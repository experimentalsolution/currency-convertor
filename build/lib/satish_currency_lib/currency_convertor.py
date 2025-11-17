import logging

from decimal import Decimal, InvalidOperation , getcontext

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CurrencyConverter:
    def __init__(self):

        #Given Currency rate
        self.CURRENCY_CONVERSION_RATES = {
            "AUDUSD": 0.8371,
            "CADUSD": 0.8711,
            "USDCNY": 6.1715,
            "EURUSD": 1.2315,
            "GBPUSD": 1.5683,
            "NZDUSD": 0.7750,
            "USDJPY": 119.95,
            "EURCZK": 27.6028,
            "EURDKK": 7.4405,
            "EURNOK": 8.6651
        }

        #Given cross matrix
        self.CROSS_VIA_MATRIX = [
    [""   , "AUD", "CAD", "CNY", "CZK", "DKK", "EUR", "GBP", "JPY", "NOK", "NZD", "USD"],
    ["AUD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"],
    ["CAD", "USD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"],
    ["CNY", "USD", "USD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "D"],
    ["CZK", "USD", "USD", "USD", "1:1", "USD", "USD", "USD", "USD", "USD", "USD", "EUR"],
    ["DKK", "USD", "USD", "USD", "EUR", "1:1", "INV", "USD", "USD", "EUR", "USD", "EUR"],
    ["EUR", "USD", "USD", "USD", "D"  , "D"  , "1:1", "USD", "USD", "USD", "USD", "D"],
    ["GBP", "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "USD", "USD", "USD",  "D"],
    ["JPY", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "USD", "USD", "INV"],
    ["NOK", "USD", "USD", "USD", "EUR", "EUR", "INV", "USD", "USD", "1:1", "USD", "EUR"],
    ["NZD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "1:1", "D"],
    ["USD", "INV", "INV", "INV", "EUR", "EUR", "INV", "INV", "D", "EUR", "INV", "1:1"]
]
    
        #Given currency precision
        self.CURRENCY_PRECISION = {
            'AUD':2,
            'CAD':2,
            'CNY':2,
            'CZK':2,
            'DKK':2,
            'EUR':2,
            'GBP':2,
            'JPY':0,
            'NOK':2,
            'NZD':2,
            'USD':2 
        }

    def apply_rates(self, currency_amount, rate_to_apply):
        '''
        This function take input as amount and rate to apply and get the exchanged amount
        :param currency_amount :Input currency
        :param rate_to_apply : the rate which needs to be applied
        :return:exchanged_amount calulated exchange rate after applying rate
        '''
        currency_amount = Decimal(currency_amount)
        rate = Decimal(rate_to_apply)
        return currency_amount * rate

    def calculate_rate(self, from_currency, to_currency):
        '''
        This function takes input as from currency and to currency and return rate
        :param from_currency : from currency
        :param to_currency : to currency
        :return: rate which needs to be applied 
        '''
        try:
            rateConfig = self.CROSS_VIA_MATRIX[self.CROSS_VIA_MATRIX[0].index(from_currency)][self.CROSS_VIA_MATRIX[0].index(to_currency)]
            #print(self.CROSS_VIA_MATRIX[0].index(from_currency))
            #print(self.CROSS_VIA_MATRIX[0].index(to_currency))
            #print(rateConfig)
        except ValueError:
            raise ValueError("Conversion rate not found for {}/{}".format(from_currency, to_currency))
        
        if rateConfig == 'D':
            return Decimal(self.CURRENCY_CONVERSION_RATES[from_currency+to_currency])
        elif rateConfig == 'INV':
            return Decimal("1") / Decimal(self.CURRENCY_CONVERSION_RATES[to_currency+from_currency])
        elif rateConfig == '1:1':
            return 1
        else:
            #print('In recursive call via'+rateConfig)
            rate1 = self.calculate_rate(from_currency, rateConfig)
            rate2 = self.calculate_rate(rateConfig, to_currency)
            return rate1 * rate2

    def convert_currency(self, from_currency, to_currency, currency_amount):
        '''
        This function converts currency from one type to another.
        
        :param from_currency: The currency to convert from.
        :param to_currency: The currency to convert to.
        :param currency_amount: The amount to convert.
        :return: converted amount if valid, or an error message.
        '''
        valid, message = self.check_valid_input(from_currency, to_currency, currency_amount)
        if valid:
            rate = self.calculate_rate(from_currency, to_currency)
            #print(f'rate is{rate}')
            precision = self.CURRENCY_PRECISION.get(to_currency, 2)
            converted_amount = self.apply_rates(currency_amount, rate).quantize(Decimal('0.' + '0' * precision))
            return converted_amount
        else:
            return message

    def check_valid_input(self, from_currency, to_currency, currency_amount):
        '''
        check if input is valid
        :param from_currency: The currency to convert from.
        :param to_currency: The currency to convert to.
        :param currency_amount: The amount to convert.
        :return: A tuple containing a boolean indicating validity and an error message (if any).
        '''
        valid = True
        error_message = []

        try:
            rateConfig = self.CROSS_VIA_MATRIX[self.CROSS_VIA_MATRIX[0].index(from_currency)][self.CROSS_VIA_MATRIX[0].index(to_currency)]
        except ValueError:
            valid = False
            error_message.append("Conversion rate not found for {}/{}".format(from_currency, to_currency))
      
        try:
            currency_amount = Decimal(currency_amount)
        except InvalidOperation:
            valid = False
            error_message.append("Currency amount is not a valid number.")

        return valid, "\n".join(error_message)

    def main(self):
        while True:
            from_currency = input('From: ')
            currency_amount = input('Amount ')
            to_currency = input('To: ')
            valid, message = self.check_valid_input(from_currency, to_currency, currency_amount)
            exchangedAmount = Decimal("0")
            if valid:
                exchangedAmount = self.convert_currency(from_currency, to_currency, currency_amount)
                print('Converted amount is: ' + str(exchangedAmount))
            else:
                print("Invalid input: {}".format(message))

            input_from_user_to_continue = input('Do you want to continue?')
            if input_from_user_to_continue in ['No', 'NO', 'n', 'N', 'no']:
                break


if __name__ == "__main__":
  
    converter = CurrencyConverter()
    '''
    converted_result = converter.convert_currency("EUR", "JPY", 123.45)
    if isinstance(converted_result, Decimal):
        print(f"Converted amount: {converted_result}")
    else:
        print(f"Invalid input: {converted_result}")
    '''
    converter.main()
    
