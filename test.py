import unittest
import reverse


class TestCase(unittest.TestCase):

    def test_reverse(self):
        Var = reverse.reverse("test")
        self.assertEqual(Var, "tset")


if __name__ == '__main__':
    unittest.main()
