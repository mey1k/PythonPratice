
import re

def intersection (arr1, arr2):

    Array = []
    strArr1 = ""
    strArr2 = ""

    for n in arr1:
        strArr1 += n
        strArr1 += ' '

    for n in arr2:
        strArr2 += n
        strArr2 += ' '

    strArr1 = strArr1[:-1]
    strArr2 = strArr2[:-1]

    checkedStr = ""

    for i in range(len(arr1)):
        p = re.compile(arr1[i])
        if p.findall(checkedStr):
            pass
        else:
            checkedStr += arr1[i] + ' '
            count = min(int(len(p.findall(strArr1))), int(len(p.findall(strArr2))))
            for i in range(count):
                    Array.append(p.findall(strArr1)[0])

    return len(Array)

def union (arr1, arr2):

    Array = []

    strArr1 = ""
    strArr2 = ""

    for n in arr1:
        strArr1 += n
        strArr1 += ' '
    
    for n in arr2:
        strArr2 += n
        strArr2 += ' '

    strArr1 = strArr1[:-1]
    strArr2 = strArr2[:-1]

    checkedStr = ""

    for i in range(len(arr2)):
        p = re.compile(arr2[i])
        if p.findall(strArr1):
            count = max(int(len(p.findall(strArr1))), int(len(p.findall(strArr2))))
            if p.findall(checkedStr[:-1]):
                pass
            else:
                checkedStr += p.findall(strArr1)[0] + ' '
                for i in range(count):
                    Array.append(p.findall(strArr1)[0])
        else: 
            Array.append(arr2[i])

    for i in range(len(arr1)):
        p = re.compile(arr1[i])
        if p.findall(strArr2):
            count = max(int(len(p.findall(strArr1))), int(len(p.findall(strArr2))))
            if p.findall(checkedStr[:-1]):
                pass
            else:
                checkedStr += p.findall(strArr2)[0] + ' '
                for i in range(count):
                    Array.append(p.findall(strArr2)[0])
        else: 
            Array.append(arr1[i])

    return len(Array)

def makeValidArray(str):

    p = re.compile('[^a-zA-Z]')
    
    Array = []

    for i in range(len(str) - 1):
        tempStr = str[i] + str[i+1]
        m = p.search(tempStr)
        if m:
            pass
        else:
            Array.append((str[i] + str[i+1]).upper())

    return Array

def solution(str1, str2):

    result = 0

    str1Array = []
    str2Array = []

    str1Array = makeValidArray(str1)
    str2Array = makeValidArray(str2)

    itscValue = intersection(str1Array, str2Array)
    unionValue = union(str1Array, str2Array)

    try:
        jaccard = itscValue / unionValue
    except:
        jaccard = 1

    
    result = 65536 * jaccard

    return print(int(result))

solution("aaaabaaa", "aaabaaaaa")
