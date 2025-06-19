# Swap the first and last elements of a list (without using temp variable)
# Input: [1, 2, 3, 4] → Output: [4, 2, 3, 1]

l1 = [1, 2, 3, 4]
length = len(l1)
l1[0], l1[length-1] = l1[length-1], l1[0]

print(l1)
