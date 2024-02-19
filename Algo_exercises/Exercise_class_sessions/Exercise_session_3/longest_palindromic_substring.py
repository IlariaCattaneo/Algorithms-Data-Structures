def palindrome(s):
    if s == s[::-1]:
        return True
    else: 
        return False
    
def lps(s):
# define a substring
# check if a substring is palindrome
# if it's palindrome return the substring
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if( j-i > 1 ):
                if palindrome(s[i:j]):
                    return s[i:j]
