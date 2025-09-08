# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

# Constraints:
# s and t consist of lowercase English letters.
-----------------------------------------------------------------------------------------------------------------

#Driver Code
if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    ans = validAnagrams(s, t)
    if(ans):
        print("s and t are valid anangrams")
    else:
        print("s and t are not valid anangrams")
      
-----------------------------------------------------------------------------------------------------------------
Approach 1 
-----------------------------------------------------------------------------------------------------------------
def validAnagrams(s:str, t:str) -> bool :
    if (len(s) != len(t)):
        return False
    sortedS = sorted(s)
    sortedT = sorted(t)
    if(sortedS == sortedT):
        return True
    return False

T.C : O(nlogn)
S.C: O(n)
-----------------------------------------------------------------------------------------------------------------
Approach 2
-----------------------------------------------------------------------------------------------------------------
def validAnagrams(s:str, t:str) -> bool :
    if (len(s) != len(t)):
        return False      
    dict = {}
  
    #for loop on the first word
    for i in s:
        if i in dict:
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    print(dict)
  
    #for loop on the first word
    for i in t:
        if i in dict:
            dict[i] = dict[i]-1
        else:
            return False
    print(dict)

    #for loop on doct
    for i in dict:
        if dict[i] == 0:
            continue
        else:
            return False
    return True
  
T.C : O(log(m+n))
S.C: O(1)
