import numpy as np

a = np.array([[0,1,2],[2,1,0]])

print(np.mean(a))                   # np.mean(a, axis, dtype, out, keepdims)
print(np.mean(a, axis = 0))         # 평균
print(np.mean(a, axis = 1))         # axis는 평균값을 구하기 위한 축

print(np.var(a))                    # 분산 np.var(~~) -> 상동,  표준편차np.std도 동일
print(np.cov(a, ddof = 0))
print(np.cov(a, ddof = 1))
print(np.corrcoef(a)[0,1])

# 공분산 np.cov(m, y, rowvar, bias, ddof, fweights, aweights)
# row는 variable, column은 observation / y는 추가적인 변수와 관측치
# rowvar 이 False면 변수와 관측지가 반대로 됨
# bias 가 False면 N-1에 의해 normalization 진행, 반대면 N에 의해
# ddof가 젤 소름인 부분인데, 따로 만지지 않으면 ddof는 1이 되어 불편분산(n-1로 나누기)을 구한다. 우리가 아는 표본분산 하려면 ddof = 0 설정하자. 이거찾느라 30분썼네
# 공분산도 행렬로 나오는데, [0][1], [1][0]이 공분산, [0][0]과 [1][1]은 각 배열의 분산이 된다.
# Cov[X,X] = Var[X]이니까...
# 상관계수는 corrcoef가 된다.
# 나머지는 검색해서..

from numpy import random
# random.seed(0)
# random값 고정
# ㅈ건부 확률 어디서 배낀거임. conditional probability
ageppl = {30:0, 40:0, 50:0, 60:0, 70:0}
sell = {30:0, 40:0, 50:0, 60:0, 70:0}
totalsell = 0
ppl = 100000
for _ in range(ppl) :
    age = random.choice([30, 40, 50, 60, 70])
    prob = float(age)/100
    ageppl[age] += 1 
    if (random.random() < prob) :
        totalsell += 1 
        sell[age] += 1 
# 나이에 따른 구매확률. 인구수만큼 반복한다고 설정

prob30 = ageppl[30]/ppl
prob30_buy = sell[30]/ppl
print(prob30)
print(prob30_buy)
print(prob30_buy/prob30)
print(sell[30]/ageppl[30])
# 30대 중에서 30대 판매량
print(totalsell/ppl)
# 평균은 0.5 근처에서 노는게 맞다.
