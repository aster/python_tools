import csv
import math
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
breakX = []
breakY = []
indexX = []
outX = []
outY = []
tmpT = 0
dt = 100  # ms 無視
thresholdFlag = False


def appendData(i):
    global thresholdFlag
    breakX.append(x[i])
    breakY.append(y[i])
    thresholdFlag = not thresholdFlag


with open("01_035_01.csv", "r") as csv_file:
    f = csv.reader(csv_file)

    for i in f:
        x.append(math.floor(float(i[9])*1000)/1000)
        y.append(math.floor(float(i[10])*1000)/1000)

# plt.plot(x,y,lw=0.5)
# plt.show()

for i in range(len(y)):
    if (not thresholdFlag):
        if y[i] <= 2.5:
            appendData(i)

    elif thresholdFlag:
        if y[i] >= 2.5:
            appendData(i)

for i in range(len(breakY)):
    if (breakX[i] - tmpT > dt/1000):
        tmpT = breakX[i]
    else:
        breakX[i] = 0
        breakY[i] = 0

breakX = [i for i in breakX if i != 0]
breakY = [i for i in breakY if i != 0]

for i in range(len(breakY)):
    print(breakX[i], ",", breakY[i], ",")
    pass

for i in range(len(breakX)):
    indexX.append(x.index(breakX[i]))

print(indexX)


yData = np.array(y[indexX[0]:indexX[1]])
maxIndex = [i for i, x in enumerate(yData) if x == np.min(yData)]
print(maxIndex)

if (len(maxIndex) == 1):
    outX.append(indexX[0] + maxIndex[0])

else:
    outX.append(indexX[0] + math.floor((maxIndex[0]+maxIndex[-1])/2))

print(outX)
