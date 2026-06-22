
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
print(
    f"Is 'A man, a plan, a canal: Panama' a palindrome? "
    f"{is_palindrome('A man, a plan, a canal: Panama')}"
)
print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")
