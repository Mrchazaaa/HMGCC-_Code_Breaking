import binascii
import re

code = "A5 97 0E CD 3C F2 A0 F3 BF AF 24 18 FC E2 CB C9 06 6E BD 3A F2 CA B9 72 E5 CB 97 2E"

#array stores each hex seperated by space, after converting to binary string
print(code.split())

#convert each hex number to an 8 bit binary string and store in new array
data = ['{0:08b}'.format(int(i, 16)) for i in code.split()]

#concatenate all binary strings together
stringData = ''
for i in range(0, len(data)):
    stringData += str(data[i])

#split long into a list of smaller binary strings of length 7 bits
newData = re.findall(r'.{,6}''.',stringData) 

#convert each 7 bit string to ascii and display and display
myString = ""
for i in range(0, len(newData)):
    myString += chr(int(newData[i], 2)) 

print(myString)
