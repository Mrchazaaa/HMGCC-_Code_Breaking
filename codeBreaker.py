import binascii
import re

code = "A5 97 0E CD 3C F2 A0 F3 BF AF 24 18 FC E2 CB C9 06 63 BD 3A F2 CA B9 72 E5 CB 97 2E"

#array stores each hex seperated by space, after converting to binary string
print(code.split())
data = ['{0:08b}'.format(int(i, 16)) for i in code.split()]

print(data)

#add all binary strings together (removing '0b from front')
stringData = ''
for i in range(0, len(data)):
    stringData += str(data[i])[2:]

#split into a list of strings of length 7
# newData = re.findall(r'.{,6}''.',stringData) 
newData = [stringData[i:i+7] for i in range(0, len(stringData), 7)]


# for i in newData:
#     print(int(i,2))

#convert and display
myString = ""
for i in newData:
    myString += chr(int(i, 2));

print(myString)
