"""
Tests for reverse.py
"""
import reverse


class TestReverse:
    def test_reverse(self):
        assert "test" == reverse.reverse("tset")
