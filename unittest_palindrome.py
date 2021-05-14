import unittest
import palindrome
#case 1, empty              True
#case 2, 1 char             True
#case 3, even char & p      True
#case 4, even char & np     False
#case 5, odd char & p       True
#case 6, odd char & np      False
class testCaseAdd(unittest.TestCase):
    def test_empty(self):
        test_val = ""
        self.assertEqual(palindrome.is_palindrome(test_val), True)

    def test_one(self):
        test_val = "a"
        self.assertEqual(palindrome.is_palindrome(test_val), True)
    
    def test_even_p(self):
        test_val = "aaaa"
        self.assertEqual(palindrome.is_palindrome(test_val), True)
    
    def test_even_np(self):
        test_val = "aabb"
        self.assertEqual(palindrome.is_palindrome(test_val), True)#fail test should be False

    def test_odd_p(self):
        test_val = "aba"
        self.assertEqual(palindrome.is_palindrome(test_val), True)

    def test_odd_np(self):
        test_val = "abc"
        self.assertEqual(palindrome.is_palindrome(test_val), True) #fail test should be False

if __name__ == '__main__':
    unittest.main()