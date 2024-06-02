class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self._cookies + n > self._capacity:
            raise ValueError("Adding cookies would exceed the jar's capacity")
        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self._cookies < n:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
import unittest
from jar import Jar

class TestJar(unittest.TestCase):
    def test_init_default_capacity(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)

    def test_init_custom_capacity(self):
        jar = Jar(20)
        self.assertEqual(jar.capacity, 20)

    def test_init_negative_capacity(self):
        with self.assertRaises(ValueError):
            Jar(-5)

    def test_deposit(self):
        jar = Jar()
        jar.deposit(5)
        self.assertEqual(jar.size, 5)

    def test_deposit_invalid_input(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.deposit(-5)

    def test_deposit_exceed_capacity(self):
        jar = Jar(10)
        with self.assertRaises(ValueError):
            jar.deposit(15)

    def test_withdraw(self):
        jar = Jar()
        jar.deposit(8)
        jar.withdraw(3)
        self.assertEqual(jar.size, 5)

    def test_withdraw_invalid_input(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.withdraw(-5)

    def test_withdraw_not_enough_cookies(self):
        jar = Jar()
        with self.assertRaises(ValueError):
            jar.withdraw(5)

    def test_str(self):
        jar = Jar(10)
        jar.deposit(3)
        self.assertEqual(str(jar), "🍪🍪🍪")

if __name__ == "__main__":
    unittest.main()

