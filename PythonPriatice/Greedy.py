'''
문제 : 지불해야 하는 값이 362원 일 때 1원 50원 100원 짜리 동전으로 동전의 수가 가장 적게 지불하시오. 

동전 지불 문제는 그리디 알고리즘을 사용해서 풀 수 있는 아주 간단하고 직관적인 예제 중 하나 입니다. 
동전이라는 특성상 큰 단위의 동전부터 지불하면 해결 되긴 하지만 그리디 알고리즘을 통해서 구현해보면 다음과 같습니다.

'''

def min_calc(value, coin):
    a=[]
    for i in coin:
        a.append([value-i, i])
    res = a[0]
    for i in a:
        if res[0] > i[0] and i[0] > 0:
            res = i
    return res
    
coin = [1,50,100]
value = [362, 0]
dic = {}
for i in coin:
    dic[i] = 0
    
while True:
    value = min_calc(value[0],coin)
    if value[0] < 0:
        break
    else:
        dic[value[1]] += 1

print(dic)

'''
min_calc 라는 함수는 현재 금액에서 각각의 동전을 뺐을 때 가장 적은 금액이 남는 경우를 반환하는 함수 입니다.

사용되는 변수는 coin ( 동전의 종류 ) 와 value ( 지불해야 하는 금액 ), dic ( 동전의 종류별로 얼마나 사용되는지 ) 로 총 3가지 변수를 사용합니다.

while loop 문은 min_calc 를 실행 한 뒤 남은 금액들 모두가 0보다 작아지기 전까지 실행하는 함수 입니다. 실행되는 동안에는 뺀 동전에 대한 value 값을 1씩 증가시키는 기능을 수행합니다.
'''