import hw_14
import unittest

class CalcTest(unittest.TestCase):

    def test_assertEqual(self):
        self.assertEqual(hw_14.get_temp('Kharkov'), 'Celsius:1 Pressure:1010')

    def test_error_404(self):
        self.assertNotEqual(hw_14.get_temp('Kharkov'), '404')

    def test_city_not_found(self):
        self.assertNotEqual(hw_14.get_temp('Kharkov'), 'City not found.')

    def test_assertRegex(self):
        self.assertNotEqual(hw_14.get_temp('Kharkov'), 'City not found.')



if __name__ == '__main__':
    unittest.main()
