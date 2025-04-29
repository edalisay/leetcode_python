# ------------------------------------------------------------------------------------------------- #
# --------------------------------------- PROBLEM STATEMENT --------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

''' 1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''



# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ PYTHON CODE ------------------------------------------ #
# ------------------------------------------------------------------------------------------------- #

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        elif str1 == str2:
            return str1
        elif len(str1) > len(str2):
            # return str2
            return self.gcdOfStrings(str1[0:len(str1)-len(str2)], str2)
        else:
            # return str1
            return self.gcdOfStrings(str1, str2[0:len(str2)-len(str1)])





# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ TEST CASES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #


s = Solution()
print(s.gcdOfStrings("ABABAB","ABAB"))





'''
the greatest common denominator should be the longest string common between two strings

when we think of it mathematically
if:
ABAB = 4
ABABAB = 6

then gcd = AB = 2
greatest common denominator cannot be 4 but 2 (since 6 % 4 != 0), hence just because len(str1) < len(str2) doesn't mean str1 becomes the automatic gcd. 
incorrect: elif len(str1) > len(str2): return str2

in math we factor it as:
4 = 2 * 2
6 = 2 * 3

take away the greatest common factor, which is 2, pretty simple metaphor

in pseudo code: do we need to create factors of str? 
I guess no, it'd be hard to identify "factors"/"multipliers, or simply greatest succession of repeatable patterns within a string and still saving memory usage.

BUT given str1 + str2 == str2 + str 1
WE ASSUME that each of the str1 & str2 is just an iteration of the gcd in different multiples
ie the AB gcd of current use case is just thrice the iteration at str1 and twice the iteration at str2
and if str1 == str2 then each of the string is just single iteration of gcd

so we can take advantage of this. now if given 1 string is longer than the other 
we can chop parts of longer string until it satisfies str1 == str2 (ie only single iteration of gcd remains)

enter recursion
so for each iteration of the function call, our aim is to slice the longer string until str1 == str2.
if first criteria is true, we should always end up with criteria 2 eventually, until we exit the loop-like recursion  
now the question is where do we chop? do we chop the longer part of the string or the shorter part of the string? AND WHY???
ie in "ABABAB"
do we retain "ABAB" or just the "AB" before we evaluate to the next iteration of the function call.

visually, it's obvious we should retain the shorter part
but logically, we should NOT retain the longer part because this would leave us with the new string that would always == the other string

str1 = ABABAB = AB/ABAB   --> slicing
we leave behind AB instead of ABAB since ABAB would default to equal str2, in all use cases, thew new string would always default to equal the other string.

now there are two ways to slice the string:
AB/ABAB --> retaining the first part
ABAB/AB --> retaining the last part

if we retain the first few characters: str1[0:len(str1)-len(str2)]

in any case, both slicing methodology is okay, because again, the string is just a multiple iteration of the gcd.
'''