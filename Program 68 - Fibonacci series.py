# fibonacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on

terms= int(input("Enter number of terms : "))
a=0
b=1
list1=[a,b]
for i in range(0,terms-2):
    c= a+b
    list1.append(c)
    a=list1[i+1]
    b=list1[i+2]
print(list1)


