# Calculate sum of even numbers from 1 to 100 including 1 and 100
total=0
for i in range(1,101):
    if i==1 or i%2==0:
        total+=i
print(f"The sum of even numbers from 1 to 100 including 1 and 100 is : {total}")