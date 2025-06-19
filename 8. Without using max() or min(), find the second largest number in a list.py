# Without using max() or min(), find the second largest number in a list
# Input: [1, 5, 2, 4, 3] → Output: 4

list1 = [1, 5, 2, 4, 3]
# list2 = []
first = list1[0]
second= list1[0]

for num in list1:
    if num > first:
        second = first
        first = num
    elif num > second and num!=first:
        second=num

print(second)






