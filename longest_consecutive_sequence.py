# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7

-------------------------------------------------------------------------------------------------------------------------
#Driver Code
nums = [2,20,6,10,3,4,5]
length_of_longest_consecutive_seq = solve(nums)
print(length_of_longest_consecutive_seq)

-------------------------------------------------------------------------------------------------------------------------
Approach 1 BrUTE FORCE
-------------------------------------------------------------------------------------------------------------------------

def solve(numbers:list[int]) -> int:
    nums_set = set(numbers)
    nums = list(nums_set)
    lognest_consec_seq_len = 0
    for i in range(len(nums)):
        consec_seq = [nums[i]]
        for j in range(len(nums)):
            if nums[j] == consec_seq[len(consec_seq)-1]+1 :
                consec_seq.append(nums[j])
            else :
                continue
        if (lognest_consec_seq_len < len(consec_seq)) :
            lognest_consec_seq_len = len(consec_seq)
    return lognest_consec_seq_len

T.C : O(n^2)
S.C : O(n)
-------------------------------------------------------------------------------------------------------------------------
Approach 2
-------------------------------------------------------------------------------------------------------------------------

def solve(nums:list[int]) -> int:
    if not nums:
        return 0
    nums.sort()
    consec_seq_len = 1
    max_len = 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            continue
        elif nums[i] == nums[i+1]-1 :
            consec_seq_len += 1
        else :
            max_len = max(max_len, consec_seq_len)
            consec_seq_len = 1
    return max(consec_seq_len, max_len)
  
T.C : O(nlogn)
S.C : O(1)
-------------------------------------------------------------------------------------------------------------------------
Approach 3
-------------------------------------------------------------------------------------------------------------------------
def solve(numbers:list[int]) -> int:
    nums = set(numbers)
    longest_seq_len = 0
    for num in nums:
        if num-1 not in nums:
            curr = num
            count = 1
            while curr+1 in nums:
                curr = curr+1
                count = count+1
            longest_seq_len = max(longest_seq_len, count)
    return longest_seq_len

T.C : O(n)
S.C : O(n)
