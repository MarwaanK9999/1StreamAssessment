import unittest
from stringReverse import reverseString

class TestStringReverse(unittest.TestCase):

    def testReverseString(self):
        # Test with a basic string.
        self.assertEqual(reverseString("hello"), "olleh")
    
    def testReverseStringEmpty(self):    
        # Test with an empty string.
        self.assertEqual(reverseString(""), "")
    
    def testReverseStringPalindrome(self):
        # Test with a palindrome.
        self.assertEqual(reverseString("madam"), "madam")
        
    def testReverseStringSpaces(self):
        # Test with a string that contains spaces.
        self.assertEqual(reverseString("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()