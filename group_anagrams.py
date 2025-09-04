# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]

# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

-----------------------------------------------------------------------------------------------------------------------------------------
#Driver Code
if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    grouped_anagrams = group_anagrams(strs)
    print(grouped_anagrams)
-----------------------------------------------------------------------------------------------------------------------------------------
Approach 1
-----------------------------------------------------------------------------------------------------------------------------------------
def valid_anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    sortedStr1 = sorted(str1)
    sortedStr2 = sorted(str2)
    if(sortedStr1 == sortedStr2):
        return True
    else:
        return False

def group_anagrams(strs:list[str]) -> list[list[str]]:
    grouped_anagrams = []
    visited = set()
    for i in range(len(strs)):
        if strs[i] in visited:
            continue
        anagrams = [strs[i]]
        visited.add(strs[i])
        for j in range(i+1, len(strs)):
            if valid_anagram(strs[i], strs[j]):
               anagrams.append(strs[j])
               visited.add(strs[j])
        grouped_anagrams.append(anagrams)
    return grouped_anagrams

T.C: O(n^2 * mlogm)
S.C: O(m)

-----------------------------------------------------------------------------------------------------------------------------------------
Approach 2
-----------------------------------------------------------------------------------------------------------------------------------------
def group_anagrams(strs:list[str]) -> list[list[str]]:
    dict = {}
    for word in strs:
        sortedStr = ''.join(sorted(word))
        if sortedStr in dict:
            dict[sortedStr].append(word)
        else :
            dict[sortedStr] = [word]
    return list(dict.values())
  
T.C: O(n)
S.C: O(n)
