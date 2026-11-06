import unittest

from billing import split_bill


class SplitBillTest(unittest.TestCase):
    def test_even_split(self):
        self.assertEqual(split_bill(900, 3), [300.0, 300.0, 300.0])

    def test_single_person_pays_everything(self):
        self.assertEqual(split_bill(450, 1), [450.0])

    def test_shares_add_up_to_exact_total(self):
        # Bug: 100 split 3 ways charged 33.33 each, so the bill came to 99.99
        self.assertEqual(split_bill(100, 3), [33.34, 33.33, 33.33])

    def test_rejects_zero_people(self):
        with self.assertRaises(ValueError):
            split_bill(100, 0)


if __name__ == "__main__":
    unittest.main()
