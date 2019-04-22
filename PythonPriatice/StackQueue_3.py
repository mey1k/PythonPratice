
def solution(bridge_length, weight, truck_weights):
    answer = 0
    right = 0

    passingTruck = [] 
    waitingTruck = []
    prePassingTruck = []

    waitingTruck = truck_weights

    while  passingTruck or waitingTruck:
        answer += 1
        right += 1

        if (passingTruck[0] == prePassingTruck[0]):
            right += 1

        if  waitingTruck:
            if(sum(passingTruck) +  waitingTruck[0] <= weight):
               passingTruck.append(waitingTruck.pop(0))

        print(passingTruck,'    ',waitingTruck,'    ')
        
        prePassingTruck = passingTruck

    return print(answer)

#solution(100, 100, [10])
solution(	2, 10, [7, 4, 5, 6])
#solution(100,100,[10,10,10,10,10,10,10,10,10,10])
#solution(	5, 5, [1,2,3,4,5])