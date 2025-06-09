boyName= input("Enter Boy's name : ")
girlName= input("Enter Girl's name : ")
boyName=boyName.lower()
girlName=girlName.lower()
combinedName = boyName+girlName

t_TrueCount=combinedName.count("t")
r_TrueCount=combinedName.count("r")
u_TrueCount=combinedName.count("u")
e_TrueCount=combinedName.count("e")
l_LoveCount=combinedName.count("l")
o_LoveCount=combinedName.count("o")
v_LoveCount=combinedName.count("v")
e_LoveCount=combinedName.count("e")

total_true_count= t_TrueCount+r_TrueCount+u_TrueCount+e_TrueCount
total_love_count= l_LoveCount + o_LoveCount+v_LoveCount+e_LoveCount


# print(f"The Love percentage is {total_true_count}{total_love_count}%")

lovePercentage= int(str(total_true_count) + str(total_love_count))

if lovePercentage<10 or lovePercentage>90:
    print(f"The Love percentage is {lovePercentage} and you go together like coke and mentos")
elif lovePercentage>=40 and lovePercentage<=50:
    print(f"The Love percentage is {lovePercentage} and you are alright together")
else:
    print(f"The Love percentage is {lovePercentage} ")

