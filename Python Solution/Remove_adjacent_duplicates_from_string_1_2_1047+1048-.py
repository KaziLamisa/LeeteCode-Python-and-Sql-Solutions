#!/usr/bin/env python
# coding: utf-8

# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
# 
# We repeatedly make duplicate removals on S until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
# 
#  
# 
# Example 1:
# 
# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
#  
# 
# Note:
# 
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.

# In[ ]:


class Solution(object):
    def removeDuplicates1(self, S):
        """
        :type S: str
        :rtype: str
        """
        #for c in S:
            #if c*2 in S:
                #S = S.replace(c*2,"")
        
        #using stack
        for character in S:
            if stack and stack[-1]==character:
                stack.pop(-1)
            else:
                stack.append(character)
        return "".join(stack)
    
     def removeDuplicates2(self, S):
        """
        :type S: str
        :rtype: str
        """
        #for c in S:
            #if c*2 in S:
                #S = S.replace(c*2,"")
        
        #using stack
        stack=[]
        
        for character in S:
            if stack and stack[-1]==character:
                stack.pop(-1)
            else:
                stack.append(character)
        return "".join(stack)

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.removeDuplicates1("abbaca")
    print s.removeDuplicates2("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy",4)


# In[ ]:




