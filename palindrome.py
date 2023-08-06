# Given an integer x, return true if x is a palindrome, and false otherwise.


def isPalindrome(x: int) -> bool:
    x_str = str(x)
    return x_str == x_str[::-1]
