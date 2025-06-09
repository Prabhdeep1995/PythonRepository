# Inverted Triangle pattern upto number 5
# 12345
# 1234
# 123
# 12
# 1

num = 5
for i in range(num+1,1,-1):
    for j in range(1,i):
        print(j,end='')
    print()