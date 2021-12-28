import final_3
import unittest


class final3Test(unittest.TestCase):
    """"""

    def test_assertEqual_Kharkov(self):
        self.assertEqual(final_3.check_input('usd 2020-12-25'), ['usd', '20201225'])

    def test_assertNotEqual_(self):
        self.assertNotEqual(final_3.check_input('usd 2020-12-25'), '')


if __name__ == '__main__':
    unittest.main()
