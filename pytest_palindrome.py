import palindrome

def test_tempty():
    test_case = ""
    answer = palindrome.is_palindrome(test_case)
    assert answer == True

def test_single():
    test_case = "a"
    answer = palindrome.is_palindrome(test_case)
    assert answer == True

def test_even_p():
    test_case = "aa"
    answer = palindrome.is_palindrome(test_case)
    assert answer == True

def test_even_np():
    test_case = "ab"
    answer = palindrome.is_palindrome(test_case)
    assert answer == False

def test_odd_p():
    test_case = "aba"
    answer = palindrome.is_palindrome(test_case)
    assert answer == True

def test_odd_np():
    test_case = "abc"
    answer = palindrome.is_palindrome(test_case)
    assert answer == False