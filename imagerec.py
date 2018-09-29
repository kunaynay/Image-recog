from PIL import Image
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# creating RGB value for the existing images to compare
def createExamples():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersWeHave = range(0, 10)
    versionWeHave = range(1, 10)

    for eachNum in numbersWeHave:
        for eachVersion in versionWeHave:
            print(str(eachNum) + '.' + str(eachVersion))
            imgFilePath = 'images/numbers/' + str(eachNum) + '.' + str(eachVersion) + '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            print(eiar)
            lintToWrite = str(eachNum) + '::' + eiar1 + '\n'
            numberArrayExamples.write(lintToWrite)


# converting any colored image into black and white only
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr


# testing user created image with existing images
def WhatNum(filepath):
    matchedAr = []
    loadExa = open('numArEx.txt', 'r').read()
    loadExa = loadExa.split('\n')
    i = Image.open(filepath)
    iar = np.array(i)
    iarl = iar.tolist()
    inQuestion = str(iarl)

    for eachExmple in loadExa:
        if len(eachExmple) > 3:
            splitEx = eachExmple.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixQ = inQuestion.split('],')

            x = 0
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
    print(matchedAr)
    z = Counter(matchedAr)
    print(z)
    print(z[0])

    graphX = []
    graphY = []
    for eachObj in z:
        print(eachObj)
        graphX.append(eachObj)
        print(z[eachObj])
        graphY.append(z[eachObj])

    fig = plt.figure()
    ax1 = plt.subplot2grid((4, 4), (0, 0), rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4, 4), (1, 0), rowspan=3, colspan=4)
    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')

    plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    ax2.xaxis.set_major_locator(xloc)
    plt.show()


ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
im = Image.open('images/test.png')
iar = np.array(im)
ii = threshold(iar)
ii=Image.fromarray(iar)
ii.save('images/threshtest.png')
'''I want to save the result of the converted image to use it to be tested further.'''
ax1.imshow(ii)
plt.show()

WhatNum('images/threshtest.png')
# createExamples() to use the existing samples to compare
# WhatNum('images/numbers/1.6.png') test to see if existing images work
# WhatNum('images/test.png') test to see if user created image works
