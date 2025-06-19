# Write a function that returns True if a string is a palindrome, ignoring case and spaces

def checkPalindrome(s):
    s1 = ""
    for i in range(len(s)):
        if s[i] == " ":
            continue
        else:
            s1 = s1 + s[i]

    s2 = ''
    for i in range(len(s1) - 1, -1, -1):
        if s1[i] == " ":
            continue
        else:
            s2 = s2 + s1[i]
    # print(s2)
    if s1 == s2:
        return True
    else:
        return False


s ="Was it I saw".lower()
print(checkPalindrome(s))
# s1=""
# for i in range(len(s)):
#     if s[i]==" ":
#         continue
#     else:
#         s1 = s1 + s[i]
#
#
# s2 = ''
# for i in range(len(s1)-1, -1,-1):
#     if s1[i]==" ":
#         continue
#     else:
#         s2 = s2 + s1[i]
# print(s2)
# if s1 == s2:
#     print("Palimdrome")
# else:
#     print("Not")


