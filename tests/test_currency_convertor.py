import unittest
from decimal import Decimal, InvalidOperation 
from satish_currency_lib.currency_convertor import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter()

    

    def test_calculate_rate(self):
        # Test direct rate
        self.assertAlmostEqual(self.converter.calculate_rate('AUD', 'USD'), Decimal('0.8371'), places=5)

        # Test inverted rate
        self.assertAlmostEqual(self.converter.calculate_rate('USD', 'AUD'), Decimal('1.19460040616'), places=5)

        # Test 1:1 rate
        self.assertEqual(self.converter.calculate_rate('GBP', 'GBP'), Decimal('1'))

        # Test cross via rate to do currently going in infinite loop
        self.assertAlmostEqual(self.converter.calculate_rate('EUR', 'JPY'), Decimal('147.718425000'), places=5)

        # Test rate not found
        with self.assertRaises(ValueError):
            self.converter.calculate_rate('KRW', 'FJD')
    
    def test_convert_currency(self):
        # Test valid conversion
        self.assertAlmostEqual(self.converter.convert_currency('USD', 'EUR', 100), Decimal(81.20), places=2)

        # Test invalid conversion
        result = self.converter.convert_currency('KRW', 'FJD', 100)
        self.assertIsInstance(result, str)  # Check if the result is an error message string
        self.assertTrue("Conversion rate not found" in result)  # Check if the specific error message is present
    

    def test_check_valid_input(self):
        # Test valid input
        valid, message = self.converter.check_valid_input('USD', 'EUR', '100')
        self.assertTrue(valid)
        self.assertEqual(message, '')

        # Test invalid currency pair
        valid, message = self.converter.check_valid_input('USD', 'XXX', '100')
        self.assertFalse(valid)
        self.assertIn('Conversion rate not found', message)

        # Test invalid currency amount
        valid, message = self.converter.check_valid_input('USD', 'EUR', 'abc')
        self.assertFalse(valid)
        self.assertIn('Currency amount is not a valid number', message)

if __name__ == '__main__':
    unittest.main()

