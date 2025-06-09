# Program to find the largest number from a list of numbers
numbers= input("Enter numbers using comma seperated : ")
if numbers.replace(',','').replace('.','').replace('-','').isdigit():
    numList= numbers.split(",")
    listLength= len(numList)
    print(numList)
    maxNumber = float(numList[0])
    for i in range(listLength):
        numList[i]=float(numList[i])
        if numList[i]>maxNumber:
            maxNumber=numList[i]
    print("The largest number is : ",maxNumber)
else:
    print("Wrong Input")
