# ------------------------------------------------------------------------------------------------- #
# --------------------------------------- PROBLEM STATEMENT --------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

''' 605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''



# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ PYTHON CODE ------------------------------------------ #
# ------------------------------------------------------------------------------------------------- #

class Solution(object):
    def canPlaceFlowers_x(self, flowerbed, n):

        is_all_planted = False
        max_index = len(flowerbed) - 1

        for i in range(len(flowerbed)):
            if n > 0:
                if i == 0 and flowerbed[i] == 0 and i == max_index:
                    flowerbed[i] = 1
                    n -= 1
                    print('index : ' + str(i) + ' satisfied criteria 1')
                elif i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    print('index : ' + str(i) + ' satisfied criteria 2')
                elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and i == max_index:
                    flowerbed[i] = 1
                    n -= 1
                    print('index : ' + str(i) + ' satisfied criteria 3')
                elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                    print('index : ' + str(i) + ' satisfied criteria 4')
                else:
                    print('index : ' + str(i) + ' satisfied criteria 5')
                    continue

        if n == 0:
            is_all_planted = True

        return is_all_planted


# alternative, more eloquent solution:
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        len_f = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]

        i = 1
        while n > 0 and i <= len_f:
            print(f'done running index {i}, current n = {n}')
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                print(f'n = {n}  i = {i}')
            i += 1

        is_all_planted = True if n == 0 else False
        print(flowerbed)

        return is_all_planted


# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ TEST CASES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

s = Solution()
flowerbed = [0]
print(s.canPlaceFlowers(flowerbed, 1))

'''
how many indexes do you need to check at once?
current position if 0 then check if position + 1 and +2 and -1 is also 0

index:
0 1 2 3
0 1 0
1 0 1
'''