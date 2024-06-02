def main():
    greeting = input("Enter a greeting: ")
    print(value(greeting))

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
import unittest
#from bank import value

class TestValue(unittest.TestCase):
    def test_value_hello(self):
        self.assertEqual(value("Hello, world!"), 0)
        self.assertEqual(value("hello, world!"), 0)
        self.assertEqual(value("HELLO, world!"), 0)

    def test_value_h(self):
        self.assertEqual(value("Hi there"), 20)
        self.assertEqual(value("hi there"), 20)
        self.assertEqual(value("HOLA"), 20)

    def test_value_other(self):
        self.assertEqual(value("Good morning"), 100)
        self.assertEqual(value("How are you?"), 100)
        self.assertEqual(value("12345"), 100)

if __name__ == "__main__":
    unittest.main()
