'''
가장 기본적인 재귀 함수의 방법을 썼을 때 나타나는 문제이다. Function Call이 쓸데 없이 겹쳐지게 되는 상황이다. 
4, 3, 2, 1, 0 | 3, 2, 1, 0 | 2, 1, 0 | 1 

처음 fibonacci(n-1)를 하고 fibonacci(n-2)를 했을 때의 값이 저장이 되지 않기 때문에 각자 자기의 줄기를 계속 뻗고 나가게 되기 때문에 일어나는 현상이다.

시간복잡도의 c가 어떻게 나오는지 자세히 들어가지는 않겠지만, c 는 golden ratio 인 
1 + √5
----------
   2
가 나온다.

겹치는 function call들을 없애는 방법이 없을까?
'''
#def fibonacci(n):
#    if n < 2:
#        return n
#    return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(5))


'''
Memoization - O(n)
Exponential 에서 Linear하게 줄인 것은 분명 대단하지만, 
Recursion Depth에 막히는 문제가 있고, 
또한 메모에 n개 만큼의 값들을 저장해야 하기 때문에 Space Complexity 가 O(n)에 달한다.
'''
#fibonacci 함수를 직접 부르는 것이 아니라 cache를 만들어 cache에 recursion을 저장시켜 놓으면 된다.

memo = {1:1, 2:1}
def fibonacci(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

'''
Fast Multiplcation - O(n)
가장 파이써닉 한 답이라고도 불린다. 
반칙이 아닐까 싶을 정도로 깔끔하면서 좋은 성능을 보여주는 방법이다. 
메모이제이션과 비슷한 형식이지만, 차이는 Memoization은 위에서 부터 밑으로 function call을 만들어주는 과정이 있다면, 
Fast Multiplication은 그 과정을 제외하고 처음부터 하나하나씩 쌓아간다.
'''

def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b

''' 
번외..
Matrix Multiplication & Exponentiation - O(log(n))
코딩 트릭을 쓰는 것으로 사실 대부분의 문제를 해결 할 수 있는 것은 사실이다. 
하지만 최적의 결과를 찾으려면 수학을 이용해야 한다. 
사실 글쓴이도 영상 20번 돌려보며 조금 이해하게 된 것 같다. 
시간 날 때마다 선형대수와 이산수학을 공부하면 이런 알고리즘을 손쉽게 짜는 날이 오지 않을까?
'''
def mult(x,y):
    """
    행렬에 대한 곱셈 함수
    x, y = list 형태의 매트릭스
    """
    if ( len(y) == 2 ):
        a = x[0]*y[0] + x[1]*y[1]
        b = x[2]*y[0] + x[3]*y[1]
        return [a,b]
    a = x[0]*y[0] + x[1]*y[2]
    b = x[0]*y[1] + x[1]*y[3]
    c = x[2]*y[0] + x[3]*y[2]
    d = x[2]*y[1] + x[3]*y[3]
    return [a,b,c,d]

# 양수에만 적용됨
def matrix_power( x, n ):
    """
    행렬 지수 함수
    """
    # fibonacci(1) 이면 그대로 x를 반환
    if ( n == 1 ):
        return x
    # n 이 짝수일 경우
    if ( n%2 == 0 ):
        return matrix_power( mult(x, x), n//2 )
    # n 이 홀수일 경우
    return mult(x, matrix_power( mult(x, x), n//2 ) )

# fibonacci example:
A = [1,1,1,0]
v = [1,0]

print(mult(matrix_power(A, n-1), v)[0])