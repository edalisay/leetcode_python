# ------------------------------------------------------------------------------------------------- #
# --------------------------------------- PROBLEM STATEMENT --------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

''' 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ PYTHON CODE ------------------------------------------ #
# ------------------------------------------------------------------------------------------------- #


# this solution have big O notation of O(n^2) which could become problematic especially for longer lists of nums
# --> see case 4 where len(nums) = 50K
class Solution(object):
    def productExceptSelf_x(self, nums):

        products = []
        for i in range(len(nums)):
            exceptSelf = nums.copy()
            exceptSelf.pop(i)
            product = 1
            for n in exceptSelf: product *= n
            products.append(product)
            print('index: ' + str(i) + ' nums[i:i+5]: ' + str(nums[i:i+5]) + ' product: ' + str(product))
        return products




# solution with big O notation: O(n)
import random
from datetime import datetime
import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        shifted_suffix = [1] * n
        shifted_prefix = [1] * n

        for i in range(n - 2, -1, -1):
            shifted_suffix[i] = shifted_suffix[i + 1] * nums[i + 1]

        for i in range(1, n):
            shifted_prefix[i] = shifted_prefix[i - 1] * nums[i - 1]

        products = np.array(shifted_suffix) * np.array(shifted_prefix)
        return products.tolist()

# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ TEST CASES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

print('Start Time: ' + str(datetime.now()) + '\n')

# case 1
s = Solution()
print('*** Case 1 ***')
print('Input:    ' + str([1,2,3,4]))
print('Expected: ' + str([24,12,8,6]))
print('Output:   ' + str(s.productExceptSelf([1,2,3,4])) + '\n')

# case 2
print('*** Case 2 ***')
print('Input:    ' + str([-1,1,0,-3,3]))
print('Expected: ' + str([0,0,9,0,0]))
print('Output:   ' + str(s.productExceptSelf([-1,1,0,-3,3])) + '\n')

# case 3
print('*** Case 3 ***')
print('Input:    ' + str([2, 3, 4, 5]))
print('Expected: ' + str([60,40,30,24]))
print('Output:   ' + str(s.productExceptSelf([2, 3, 4, 5])) + '\n')

# case 4
print('*** Case 4 ***')
nums = [random.choice([-1, 1]) for _ in range(10**4*5)]
output = s.productExceptSelf(nums)
print('Input:    ' + str(nums[:4]) + ' --> (last 4 items in nums where len(nums) = 10^5)')
print('Output:   ' + str(output[:4]) + '\n')
print('End Time: ' + str(datetime.now()))