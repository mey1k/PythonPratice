
def nqueen(sol, N): 
    global count 
    if len(sol) == N: # 정답 배열(sol)의 길이가 N과 같아지면 sol 을 프린트한다. 
        count += 1 
        print(count, sol) 
        return 0 
    candidate = list(range(N)) # 0 부터 N-1 까지로 구성된 후보군(cadidate) 배열을 만든다. 
    for i in range(len(sol)): 
        if sol[i] in candidate: # 같은 열에 놓이는지 체크 
            candidate.remove(sol[i]) # 같은 열에 놓이면 후보군에서 제외 
        distance = len(sol) - i 
        if sol[i] + distance in candidate: # 같은 대각선 상에 놓이는지 체크 
            candidate.remove(sol[i] + distance) # 같은 대각선 상에 놓이면 후보군에서 제외 
        if sol[i] - distance in candidate: # 같은 대각선 상에 놓이는지 체크 
            candidate.remove(sol[i] - distance) # 같은 대각선 상에 놓이면 후보군에서 제외 
    if candidate != []: 
         for i in candidate: 
             sol.append(i) # 후보군의 요소를 정답 배열의 i+1 번째 요소로 설정 
             nqueen(sol, N) # 재귀적으로 다음 후보군 체크 
             sol.pop() 
    else: 
          return 0 

count = 0 
num = int(input("Input N : ")) 
for i in range(num): 
    nqueen([i], num) 

if count == 0: 
    print("No solution")

