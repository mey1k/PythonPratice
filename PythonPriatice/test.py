
def test():

    testList = [1,2]

    #pop first, last
    print(testList.pop(0))
    print(testList.pop())

    #empty check
    if not testList:
        print("This is empty list")
    if len(testList) == 0:
        print("This is empty list")

test()
