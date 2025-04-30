# ------------------------------------------------------------------------------------------------- #
# --------------------------------------- PROBLEM STATEMENT --------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

''' 345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"



Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''



# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ PYTHON CODE ------------------------------------------ #
# ------------------------------------------------------------------------------------------------- #

class Solution(object):
    def reverseVowels(self, s):

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_vowels = []
        s_range = range(len(s))
        newWord = []
        for i in s_range:
            if s[i] in vowels:
                s_vowels.append(s[i])

        for i in s_range:
            if s[i] in vowels:
                newWord.append(s_vowels[len(s_vowels) - 1])
                s_vowels.pop()
            else:
                newWord.append(s[i])

        return ''.join(newWord)


# ------------------------------------------------------------------------------------------------- #
# ------------------------------------------ TEST CASES ------------------------------------------- #
# ------------------------------------------------------------------------------------------------- #

s = Solution()
print(s.reverseVowels("leetcode"))