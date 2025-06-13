#Capatalize first and last alphabet of every word and reverse the string
# WAP# User input - "my name is kartar singh" O/P -> "YM EmaN SI RatraK HgniS"

name = 'my name is kartar singh'
nameList= name.split(" ")
length = len(nameList)

newString=''
for i in range(length):
     s=nameList[i]
     l = len(s)
     for j in range(l-1,-1,-1):
          if j==0 or j==l-1:
               newString = newString + s[j].upper()
          else:
               newString =newString + s[j].lower()
     newString = newString + " "
print(newString)