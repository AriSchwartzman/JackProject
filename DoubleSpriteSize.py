# I just used https://www.convzone.com/decimal-to-binary/ to do the decimal to binary conversion
def twos_comp(value, bits):
    """compute the 2's complement of an int value with a given number of bits"""
    if (value & (1 << (bits - 1))) != 0: # if the sign bit is set (most significant bit is 1)
        value = value - (1 << bits)      # compute negative value
    return value

string = """11000000
11000000
1111110000
11000000
11000000
11111111000
1111110000
1111110000
111111111100
11111111000
11111111000
11111111000
1111111111110
11111111111111"""

binList = string.split("\n")
col0 = []
col1 = []

for i in binList:
    i = i[::-1]
    newBin = ""
    for j in i:
        newBin += j*2
        if(len(newBin) == 16):
            newBin += " "
    
    while(newBin.endswith("0")):
        newBin = newBin[:-1]
    
    
    tempList = newBin.split(" ")
    
    for i in range(len(tempList)):
        tempList[i] = tempList[i][::-1]
        if(len(tempList[i]) != 0):
            out = twos_comp(int(tempList[i], 2), len(tempList[0]))
        else:
            out = 0
            
        if(i == 0):
            col0.append(out)
            col0.append(out)
        else:
            col1.append(out)
            col1.append(out)
        # print(out)
        # print(out)
    
    if len(col0) > len(col1):
        col1.append(0)
        col1.append(0)
    
counter = 1
for i in col0:
    print(str(i))
    counter += 1

for i in col1:
    print(str(i))
    counter += 1
