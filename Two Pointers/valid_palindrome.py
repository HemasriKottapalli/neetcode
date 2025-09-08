# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

# Constraints:

# 1 <= s.length <= 1000
# s is made up of only printable ASCII characters.
----------------------------------------------------------------------------------------------------------------
#Driver Code
s = "Was it a car or a cat I hsaw?"
ans = is_palindrome(s)
print(ans)
----------------------------------------------------------------------------------------------------------------
Two Pointer Approach
----------------------------------------------------------------------------------------------------------------
def is_palindrome(s : str) -> bool:
    string = ''.join(filter(str.isalnum, s))
    string = string.lower()
    i=0
    j=len(string)-1
    flag = True
    while(i<=j):
        if(string[i] != string[j]):
            flag = False
        i+=1
        j-=1
    return flag

T.C : O(n)
S.C : O(1)
