
def solution(bridge_length, weight, truck_weights):
    answer = 0
    count = 0

    passingTruck = [] 
    waitingTruck = []
    passedTruck = []

    waitingTruck = truck_weights

    while  passingTruck or waitingTruck:
        answer += 1

        if count >= bridge_length and bridge_length < answer:
            passedTruck.append (passingTruck.pop(0))
            count -= bridge_length

        if  waitingTruck:
            if(sum(passingTruck) +  waitingTruck[0] <= weight):
               passingTruck.append(waitingTruck.pop(0))               

        count += len(passingTruck) 

        print(answer,'      ',passedTruck,'     ', passingTruck,'    ', waitingTruck)

    return print(answer)

#solution(100, 100, [10])
#solution(2, 10, [7, 4, 5, 6])
#solution(100,100,[10,10,10,10,10,10,10,10,10,10])
#solution(5, 5, [1,2,3,4,5])
solution(5,5,[1,2,3,2])