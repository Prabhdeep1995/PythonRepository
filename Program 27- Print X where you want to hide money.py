# Print X where you want to hide money
row1= ['😊','😊','😊']
row2= ['😊','😊','😊']
row3= ['😊','😊','😊']
finalList=[row1,row2,row3]

num=input("Enter the position where you want to hide money : ")
row=int(num[0])
column=int(num[1])

subList =finalList[row-1]
subList[column-1]='❌'
# finalList[row-1][column-1]='X'

print(f"{row1}\n{row2}\n{row3}")










# finalList=[[1,2,3],[11,22,33],[111,222,333]]
# list1=[2,3,4]
# length= len(finalList)
# # print(length)
# num=input("Enter two digit number : ")
# a=int(num[0])
# b=int(num[1])
#
# subList =finalList[a-1]
# # print(subList)
# subList[b-1]='X'
# # print(subList)
#
# print(finalList)

