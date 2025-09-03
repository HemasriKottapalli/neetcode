# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000
--------------------------------------------------------------------------------------------------------------------------
#Driver Code
if __name__ == "__main__":
    nums = [3,4,5,6]
    target = 7
    solve(nums, target)

--------------------------------------------------------------------------------------------------------------------------
Approach 1
--------------------------------------------------------------------------------------------------------------------------
def solve(nums:list[int], target:int) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                print(nums[i], nums[j])
                return True
    return False

--------------------------------------------------------------------------------------------------------------------------
Approach 2
--------------------------------------------------------------------------------------------------------------------------
  def binarySearch(nums:list[int], comp:int, start:int, end: int):
    mid = (start + end) //2
    
    while (start <= end):
        if (nums[mid] == comp):
            return comp
        elif (nums[mid] < comp):
            start = mid+1
        else:
            end = mid-1
        mid = (start + end) //2

    return -1


def solve(nums:list[int], target:int):
   nums = sorted(nums)
   
   for i in range(len(nums)):
       comp = target - nums[i]
       comp = binarySearch(nums, comp, i+1, len(nums)-1)
       if(comp != -1):
            return (nums[i], comp)
   return None
