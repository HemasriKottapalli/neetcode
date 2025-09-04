# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]

# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
--------------------------------------------------------------------------------------------------------------------------------
#Driver Code
if __name__ == "__main__":
   nums = [1,2,2,3,3,3]
   k=2
   top_k_freequent_elements = find_top_k_freequent_elements(nums, k)
   print(top_k_freequent_elements)

--------------------------------------------------------------------------------------------------------------------------------
Approach 1
--------------------------------------------------------------------------------------------------------------------------------
def find_top_k_freequent_elements(nums, k):
    dict = {}
    ans = []
    for i in nums:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    for i in range(k):
        max_freq_key = max(dict, key=dict.get)
        ans.append(max_freq_key)
        del dict[max_freq_key]
    return ans

T.C: O(n)  
S.C : O(n)
