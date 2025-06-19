# 1. Reverse Words in a String (without using .split() or .reverse())
# Input: "I love Python" # Output: "Python love I"

s = "I love Python"
ss=''
l1 = []
length = len(s)

for i in range(length-1,-1,-1):
    if s[i] == " ":
        print(ss, end=" ")
        ss=""
    else:
        ss = ss + s[i]
print(ss)






# s1=""
# len = len(s)
# new_length=0
# for i in range(len-1,-1,-1):
#     s1 = s1 + s[i]
#     new_length+=1
#     if s[i] == " ":
#         for j in range(new_length-1,-1,-1):
#             print(s1[j])







