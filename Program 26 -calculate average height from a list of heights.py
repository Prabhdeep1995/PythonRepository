# Program to calculate average height from a list of heights

# heightList = [160,165,140,170,175]
# count =0
# sum=0
# for i in heightList:
#     sum= sum + i
#     count+=1
# average = sum/count
# print(average)


heights = input("Enter heights : ")
if heights.replace(',','').replace('.','').isdigit():
    heightList = heights.split(',')
    print(heightList)
    heightSum = 0
    count = 0
    for i in heightList:
        heightSum = heightSum + float(i)
        count += 1
    avg = heightSum / count
    print(round(avg))
else:
    print('Invalid input')


