# Count Vowels in the entered string

sentence = input("Enter any Sentence : ")
count = 0
for i in sentence:
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
        count+=1
    else:
        continue
print(f"The count of vowels in the sentence - {sentence} is {count}")