
import unittest
from kibble_calculator import kibble_amount


class TestKibble(unittest.TestCase):
    def test_base_case(self):
        dogs = {'small': 3, 'medium': 1, 'large': 4}
        leftover = 15
        result = kibble_amount(dogs, leftover)
        self.assertEqual(result, 186)

    def test_no_dogs(self):
        dogs = {'small': 0, 'medium': 0, 'large': 0}
        leftover = 15
        result = kibble_amount(dogs, leftover)
        self.assertEqual(result, 0)

    def test_no_leftover(self):
        dogs = {'small': 3, 'medium': 1, 'large': 4}
        leftover = 0
        result = kibble_amount(dogs, leftover)
        self.assertEqual(result, 204)

    def test_many_dogs(self):
        dogs = {'small': 432, 'medium': 865, 'large': 673}
        leftover = 200
        result = kibble_amount(dogs, leftover)
        self.assertEqual(result, 49932)

    def test_fraction_dogs(self):
        dogs = {'small': 4.5, 'medium': 8, 'large': 7.8}
        leftover = 200
        with self.assertRaises(ValueError):
            kibble_amount(dogs, leftover)

    def test_negative_leftover(self):
        dogs = {'small': 4.5, 'medium': 8, 'large': 7.8}
        leftover = -80
        with self.assertRaises(ValueError):
            kibble_amount(dogs, leftover)

    def test_huge_leftover(self):
        dogs = {'small': 3, 'medium': 1, 'large': 4}
        leftover = 999
        result = kibble_amount(dogs, leftover)
        self.assertEqual(result, 0)

    def test_non_number_dog(self):
        dogs = {'small': "a", 'medium': 1, 'large': 4}
        leftover = 999
        with self.assertRaises(ValueError):
            kibble_amount(dogs, leftover)

    def test_non_number_leftover(self):
        dogs = {'small': 3, 'medium': 1, 'large': 4}
        leftover = "a"
        with self.assertRaises(TypeError):
            kibble_amount(dogs, leftover)


if __name__ == '__main__':
    unittest.main()
