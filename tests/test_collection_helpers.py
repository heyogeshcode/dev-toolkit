"""Unit tests for collection helpers."""

import unittest
from utils.collection_helpers import chunk, flatten, unique_by, group_by


class TestCollectionHelpers(unittest.TestCase):
    def test_chunk(self):
        self.assertEqual(chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])

    def test_unique_by(self):
        data = [{"id": 1, "val": "a"}, {"id": 2, "val": "b"}, {"id": 1, "val": "c"}]
        res = unique_by(data, lambda x: x["id"])
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]["id"], 1)

    def test_group_by(self):
        data = ["apple", "banana", "avocado", "blueberry"]
        groups = group_by(data, lambda x: x[0])
        self.assertEqual(len(groups["a"]), 2)
        self.assertEqual(len(groups["b"]), 2)


if __name__ == "__main__":
    unittest.main()
