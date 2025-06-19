# Count an occurence of each element in a list

num1 = [1,5,6,2,1,5,3,2,1]
num2 = []

for i in num1:
    count = 0
    if i not in num2:
        for j in num1:
            if i==j :
                count+=1
                num2.append(i)
        print(f"The count of {i} is {count}")