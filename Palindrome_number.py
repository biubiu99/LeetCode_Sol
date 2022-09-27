
def isPalindrome(self, x: int) -> bool:
    x_string: str = str(x)
    x_reverse: str = x_string[::-1]
    if x_reverse == x_string:
        return True
    else:
        return False
