

a = int(input("Enter First number: "))
b = int(input("Enter second number: "))
flag = input("Enter Flag value True or False: ")
flag = flag.strip().lower() == "true"
def checkStatus(a,b,flag):
    if (a>0 and b<0 ) and flag == False:
        return True
    elif (a<0 and b>0 ) and flag == False:
        return True
    elif (a<0 and b<0) and flag == True:
        return  True
    else:
        return False

statusValue = checkStatus(a,b,flag)
print(statusValue)

