import unittest
from palindromeChecker import isPalindrome

class TestPalindromeChecker(unittest.TestCase):

    def testPalindrome(self):
        # Test basic palindromes.
        self.assertTrue(isPalindrome("madam"))
        self.assertTrue(isPalindrome("racecar"))

    def testNonPalindrome(self):
        # Test non-palindromes.
        self.assertFalse(isPalindrome("hello"))
        self.assertFalse(isPalindrome("python"))

    def testPalindomeEmpty(self):
        # Test a case of an empty string.
        self.assertTrue(isPalindrome(""))

    def testPalindromeSingle(self):
        # Test a case which can have a single character that will always be a palindrome.
        self.assertTrue(isPalindrome("a"))

if __name__ == '__main__':
    unittest.main()