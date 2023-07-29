"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # listdeki butun strlari liste cevirerem, daha sonra her birinin 0ci indexdeki elemenrlerini bir-biri ile yoxlayaram
        flag = ""
        for i in range(len(strs)):
            fi = list(strs[i].strip())
            print("fi=", fi)
            for j in range(i+1, len(strs)):
                ji = list(strs[j].strip())
                print("ji=", ji)

                for c in fi:
                    for a in ji:
                        print("c=", c)
                        print("a=", a)
                        if c == a:
                            flag += c
                            
                            print("flag=", flag)
                        else:
                            return "asd"
                
        return flag

s = Solution()
result = s.longestCommonPrefix(strs = ["flower","flow","flight"])
print(result)