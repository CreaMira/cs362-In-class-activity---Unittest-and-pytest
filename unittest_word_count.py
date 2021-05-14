import unittest
import word_count
#case 1, empty                      0
#case 2, 1 char                     1
#case 3, "This is an activity"      4

class testCaseAdd(unittest.TestCase):
    def test_empty(self):
        test_val = ""
        self.assertEqual(word_count.count_word(test_val), 0)

    def test_char(self):
        test_val = "a"
        self.assertEqual(word_count.count_word(test_val), 1)
    
    def test_sentence(self):
        test_val = "This is an activity"
        self.assertEqual(word_count.count_word(test_val), 3) #fail test should be 4



if __name__ == '__main__':
    unittest.main()