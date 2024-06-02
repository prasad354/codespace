def main():
    fraction = input("Enter a fraction in X/Y format: ")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(e)

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return round(x / y * 100)
    except ValueError:
        raise ValueError("Invalid input format. Please provide X/Y format.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
import unittest
#from fuel import convert, gauge

class TestFuel(unittest.TestCase):
    def test_convert_valid(self):
        self.assertEqual(convert("1/2"), 50)
        self.assertEqual(convert("3/4"), 75)
    
    def test_convert_invalid_format(self):
        with self.assertRaises(ValueError):
            convert("1:2")
    
    def test_convert_invalid_numerator(self):
        with self.assertRaises(ValueError):
            convert("2/1")
    
    def test_convert_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            convert("1/0")
    
    def test_gauge_e(self):
        self.assertEqual(gauge(0), "E")
        self.assertEqual(gauge(1), "E")
    
    def test_gauge_f(self):
        self.assertEqual(gauge(99), "F")
        self.assertEqual(gauge(100), "F")
    
    def test_gauge_percentage(self):
        self.assertEqual(gauge(50), "50%")
        self.assertEqual(gauge(75), "75%")

if __name__ == "__main__":
    unittest.main()
