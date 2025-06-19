# num = 77
# c = 0
# for i in range(0,num+1):
#     a = i%10
#     b= i//10
#     if a== 7 or b==7 :
#         c+=1
#
# print(c)

num = 77
c=0
for i in range(1,num+1):
    temp = str(i)
    for char in temp:
        if int(char)== 7:
            c+=1
print(c)