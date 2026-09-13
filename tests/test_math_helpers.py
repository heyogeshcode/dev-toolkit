"""Unit tests for mathematical calculations."""

import unittest
from utils.math_helpers import clamp, lerp, mean, median


class TestMathHelpers(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(-5, 0, 10), 0)
        self.assertEqual(clamp(15, 0, 10), 10)

    def test_lerp(self):
        self.assertAlmostEqual(lerp(0, 100, 0.5), 50.0)
        self.assertAlmostEqual(lerp(10, 20, 0.25), 12.5)

    def test_mean(self):
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5]), 3.0)

    def test_median(self):
        self.assertAlmostEqual(median([1, 3, 5]), 3.0)
        self.assertAlmostEqual(median([1, 2, 3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
