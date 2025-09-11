# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:

# 3 <= nums.length <= 1000
# -10^5 <= nums[i] <= 10^5

------------------------------------------------------------------------------------------------
#Driver Code
nums = [1,4,-1,1,3,-2]
print(get_triplets(nums))
------------------------------------------------------------------------------------------------
Approach 1:
------------------------------------------------------------------------------------------------
def get_triplets(nums : list[int]):
    ans = set()
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 10:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(x) for x in ans]

T.C : O(n^3)
S.C : O(n)
------------------------------------------------------------------------------------------------
Approach 2:
------------------------------------------------------------------------------------------------
def get_triplets(nums : list[int]) -> list[list[int]]:
    ans = set()
    nums.sort()
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        
        while left < right:
            if nums[i]+nums[left]+nums[right] == 0:
                ans.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[i]+nums[left]+nums[right] < 0:
                left += 1
            else:
                right -= 1
    return [x for x in ans]

T.C : O(n^2)
S.C : O(n)
