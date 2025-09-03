# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


--------------------------------------------------------------------------------------------------------------
Driver code
--------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    ans = hasDuplicates(nums)
    if(ans):
        print("this list of nums contain duplicates")
    else:
        print("this list of nums doesn't contain duplicates")


--------------------------------------------------------------------------------------------------------------
Approach 1:
--------------------------------------------------------------------------------------------------------------

def hasDuplicates(nums: int) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] == nums[j]):
                return True
    return False

T.C: O(n^2)
S.C: O(1)
--------------------------------------------------------------------------------------------------------------
Approach 2:
--------------------------------------------------------------------------------------------------------------
def hasDuplicates(nums: int) -> bool:
    set1 = set(nums)
    if(len(nums) > len(set1)):
        return True
    else:
        return False

T.C: O(n)
S.C: O(n)
--------------------------------------------------------------------------------------------------------------
Approach 3:
--------------------------------------------------------------------------------------------------------------

def hasDuplicates(nums: int) -> bool:
    new_nums = sorted(nums)
    for i in range(len(nums)-1):
        if (nums[i] == nums[i+1]):
            return True
    return False

T.C: O(nlogn)
S.C: O(1)
