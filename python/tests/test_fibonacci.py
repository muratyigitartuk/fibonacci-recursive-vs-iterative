import unittest
from python.fibonacci import fib_recursive_memo, fib_iterative


class TestFibonacci(unittest.TestCase):
    def test_small_values(self):
        for n in range(0, 21):
            self.assertEqual(fib_iterative(n), fib_recursive_memo(n))

    def test_input_validation(self):
        with self.assertRaises(ValueError):
            fib_iterative(-1)
        with self.assertRaises(TypeError):
            fib_iterative(1.5)
        with self.assertRaises(ValueError):
            fib_recursive_memo(-1)
        with self.assertRaises(TypeError):
            fib_recursive_memo("10")


if __name__ == "__main__":
    unittest.main()