# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.
----------------------------------------------------------------------------------------------------------------
def encode(strs:list[str]) -> str:
    encoded_string = ''
    for word in strs:
        length = str(len(word))
        encoded_string += f"{length}#{word}"
    return encoded_string

def decode(string : str) -> list[str]:
    decoded_list = []
    i = 0
    while(i < len(string)):
        length = ''
        while(string[i] != '#'):
            length += string[i]
            i += 1
        length = int(length)
        j = i+1
        k = i + length + 1
        str_local = string[j:k]
        decoded_list.append(str_local)
        i = k
    return decoded_list 
  
#Driver Code  
strs = ["we","say",":","yes","!@#$%^&*()"]
encoded_str = encode(strs)
print(decode(encoded_str)) 
print(encoded_str)

T.C : O(n)
S.C : O(n)
