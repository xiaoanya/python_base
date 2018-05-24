# class Solution:
#    def replaceSpace(self,s):
        
#     #   rerurn map(lambda x : " %20" x==''  ,s)
     
#         b = ""
#         for i in range(len(s)):
#             if s[i] == " ":
#                 b += "%20"
#             else:
#                 b += s[i]
#         return b

# S=Solution()
# print(S.replaceSpace('Hello World'))

class Solution:
    def replaceSpace(self,s):
        b = ''
        for x in range(len(s)):
            if s[x] == ' ':
                b += '%20'
            else:
                b += s[x]
        return b
S=Solution()
print(S.replaceSpace('Hello World'))
        
