def main():
    word = input("Enter a word: ")
    print(shorten(word))

def shorten(word):
    vowels = 'AEIOUaeiou'
    return ''.join(char for char in word if char not in vowels)

if __name__ == "__main__":
    main()
import unittest
#from twttr import shorten

class TestShorten(unittest.TestCase):
    def test_shorten_empty_string(self):
        self.assertEqual(shorten(""), "")

    def test_shorten_no_vowels(self):
        self.assertEqual(shorten("hello"), "hll")

    def test_shorten_only_vowels(self):
        self.assertEqual(shorten("AEIOU"), "")

    def test_shorten_mixed_case(self):
        self.assertEqual(shorten("aEiOu"), "")

    def test_shorten_mixed_case_with_consonants(self):
        self.assertEqual(shorten("HelloWorld"), "HllWrld")

if __name__ == "__main__":
    unittest.main()
