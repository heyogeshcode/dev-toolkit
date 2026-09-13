"""Unit tests for validator helpers."""

import unittest
from utils.validator_helpers import is_email, is_ipv4, is_uuid


class TestValidatorHelpers(unittest.TestCase):
    def test_is_email(self):
        self.assertTrue(is_email("dev@example.com"))
        self.assertTrue(is_email("user.name+tag@sub.domain.org"))
        self.assertFalse(is_email("invalid-email"))
        self.assertFalse(is_email("@missinguser.com"))

    def test_is_ipv4(self):
        self.assertTrue(is_ipv4("127.0.0.1"))
        self.assertTrue(is_ipv4("192.168.1.1"))
        self.assertFalse(is_ipv4("256.0.0.1"))
        self.assertFalse(is_ipv4("not.an.ip.address"))

    def test_is_uuid(self):
        self.assertTrue(is_uuid("123e4567-e89b-12d3-a456-426614174000"))
        self.assertFalse(is_uuid("not-a-uuid"))


if __name__ == "__main__":
    unittest.main()
