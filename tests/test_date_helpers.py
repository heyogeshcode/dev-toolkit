"""Unit tests for datetime helper utilities."""

import unittest
from datetime import datetime, timezone
from utils.date_helpers import parse_iso, format_readable, humanize_seconds


class TestDateHelpers(unittest.TestCase):
    def test_parse_iso(self):
        dt = parse_iso("2026-09-13T10:00:00+00:00")
        self.assertIsNotNone(dt)
        self.assertEqual(dt.year, 2026)
        self.assertIsNone(parse_iso("invalid-date-string"))

    def test_format_readable(self):
        dt = datetime(2026, 9, 13, 10, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(format_readable(dt), "2026-09-13 10:00:00 UTC")

    def test_humanize_seconds(self):
        self.assertEqual(humanize_seconds(45), "45s")
        self.assertEqual(humanize_seconds(125), "2m 5s")
        self.assertEqual(humanize_seconds(3600), "1h 0m")


if __name__ == "__main__":
    unittest.main()
