# Triangle pattern upto number 5
# 1
# 12
# 123
# 1234
# 12345

num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end='')
    print()