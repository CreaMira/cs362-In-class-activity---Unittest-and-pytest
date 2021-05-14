def is_palindrome(input_str):
    #if the string is odd we can ignore the middle one
    #we only need to compare each two of the element in the string
    for i in range (0, int(len(input_str)/2)):
        if input_str[i] != input_str[len(input_str)-i-1]:
            return False
    
    return True