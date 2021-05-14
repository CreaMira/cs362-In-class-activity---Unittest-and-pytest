import word_count

def test_tempty():
    test_case = ""
    answer = word_count.count_word(test_case)
    assert answer == 0

def test_single():
    test_case = "a"
    answer = word_count.count_word(test_case)
    assert answer == 1

def test_even_p():
    test_case = "This is an activity"
    answer = word_count.count_word(test_case)
    assert answer == 3                          #fail test should be 4

