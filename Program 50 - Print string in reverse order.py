# Print string in reverse order

s = input("Enter any string : ")
rev=''
for i in range(len(s)-1,-1,-1):
    rev =rev+ s[i]
print(f"The reverse of {s} string is {rev}")

