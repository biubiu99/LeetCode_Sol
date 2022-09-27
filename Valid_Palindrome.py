def isPalindrome(self, s: str) -> bool:
    s: str = s.lower()
    result = ''
    for character in s:
        if character.isalnum():
            result += character

    if result == result[::-1]:
        return True
    else:
        return False