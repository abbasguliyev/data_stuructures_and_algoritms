"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Follow up: Could you solve it without converting the integer to a string?
"""
# First way
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            reverse_list = list()
            while x > 0:
                residual = x % 10
                reverse_list.append(residual)
                x = x // 10
            num_list = reverse_list[::-1]
            return num_list == reverse_list
        elif x == 0:
            return True
        else:
            return False

# Second Way
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         return x == x[::-1]

r = Solution().isPalindrome(x=121)
print(f"{r=}")