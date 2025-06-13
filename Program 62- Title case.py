# Capatalize  first alphabet of each word
# Input = 'hello world'
# Output = 'Hello World'


name = 'hello world'
nameList= name.split(" ")
length = len(nameList)

newString=''
for i in range(length):
     s=nameList[i]
     l = len(s)
     for j in range(l):
          if j==0:
               newString = newString + s[j].upper()
          else:
               newString =newString + s[j].lower()
     newString = newString + " "
print(newString)


