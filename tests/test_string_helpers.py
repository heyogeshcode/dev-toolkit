"""Unit tests for string processing helper utilities."""

import unittest
from utils.string_helpers import slugify, truncate, split_words


class TestStringHelpers(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World!"), "hello-world")
        self.assertEqual(slugify("  Python 3.12 -- Rocks! "), "python-312-rocks")

    def test_truncate(self):
        self.assertEqual(truncate("Short text", 20), "Short text")
        self.assertEqual(truncate("Very long sentence to shorten", 10), "Very lo...")

    def test_split_words(self):
        self.assertEqual(split_words("one, two; three!"), ["one", "two", "three"])


if __name__ == "__main__":
    unittest.main()
