# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Driver Code
nums = [1,2,4,6]
ans_arr = solve(nums)
print(ans_arr)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Approach 1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def solve(nums : list[int]) -> list[int]:
    arr_product = 1
    no_of_zeros = 0
    index_of_zero_element = 0
    ans_arr = [0] * len(nums)

    for i in range(len(nums)):
        if nums[i] == 0 :
            no_of_zeros += 1
            index_of_zero_element = i
        else :
            arr_product *= nums[i]
            
    if no_of_zeros == 0:
        for i in range(len(nums)):
            ans_arr[i] = arr_product//nums[i]
    elif no_of_zeros == 1:
        ans_arr[index_of_zero_element] = arr_product
    
    return ans_arr

T.C : O(n)
S.C : O(n)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Approach 2
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def solve(nums : list[int]):
    prefix_arr = [1] * len(nums)
    suffix_arr = [1] * len(nums)
    ans_arr = [0] * len(nums)
    
    #build prefix array
    for i in range(1, len(nums)):
        prefix_arr[i] = prefix_arr[i-1] * nums[i-1]
        
    #build suffix array
    for i in range(len(nums)-2, -1, -1):
        suffix_arr[i] = suffix_arr[i+1] * nums[i+1]

    #build ans array
    for i in range(len(nums)):
        ans_arr[i] = prefix_arr[i] * suffix_arr[i]
    
    return ans_arr

T.C : O(n)
S.C : O(n)
