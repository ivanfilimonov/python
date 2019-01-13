import unittest

from main.hw1.swap_max_and_min import swap_max_and_min


class TestBetween(unittest.TestCase):

    def test_swap_max_and_min(self):
        self.assertEqual(swap_max_and_min([1, 2, 3]), [3, 2, 1])
        self.assertEqual(swap_max_and_min([-78, 23, 333]), [333, 23, -78])
        self.assertEqual(swap_max_and_min([-78, -23, -50]), [-23, -78, -50])
        with self.assertRaises(TypeError, msg='swap_max_and_min([-78, "asd", -50])'):
            swap_max_and_min([-78, "asd", -50])

        with self.assertRaises(ValueError, msg="swap_max_and_min([43, 43, -50])"):
            swap_max_and_min([43, 43, -50])


if __name__ == "__main__":
    unittest.main()