
def solution(bridge_length, weight, truck_weights):
    shortestTime = 0

    passingTruck = [] 
    waitingTruck = []

    waitingTruck = truck_weights
    passingTruck = [0]*bridge_length

    while  passingTruck:
        shortestTime += 1
        passingTruck.pop(0)

        if  waitingTruck:
            if(sum(passingTruck) +  waitingTruck[0] <= weight):
               passingTruck.append(waitingTruck.pop(0))
            else:
               passingTruck.append(0)

        print(shortestTime, '   ', passingTruck, '    ', waitingTruck)

    return print(shortestTime)


#solution(100, 100, [10])
#solution(2, 10, [7, 4, 5, 6])
#solution(100,100,[10,10,10,10,10,10,10,10,10,10])
#solution(5, 5, [1,2,3,4,5])
solution(5,5,[1,2,3,2])