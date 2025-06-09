# Use random function to find who will pay the bill
import random
names= input("Enter names seperated by comma : ")
names_list= names.split(",")
print(names_list)
len=len(names_list)
random_choicendex=random.randint(0,len-1)
print(f"{names_list[random_choicendex]} will pay the bill")

