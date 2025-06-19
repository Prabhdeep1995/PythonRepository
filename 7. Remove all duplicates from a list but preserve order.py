# Remove all duplicates from a list but preserve order
# Input: [1, 2, 1, 3, 2, 4] → Output: [1, 2, 3, 4]

l1 = [1, 2, 1, 3, 2, 4]
l2 = []
c=0
for i in l1:
    if i in l2:
        continue
    else:
        l2.append(i)
print(l2)


