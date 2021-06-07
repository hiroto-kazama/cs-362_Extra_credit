import unittest
import reverse

class TestCase(unittest.TestCase):

    def test_reverse(self):
        Var = reverse.reverse("test is done")
        self.assertEqual(Var, "enod si tset")


if __name__ == '__main__':
    unittest.main()