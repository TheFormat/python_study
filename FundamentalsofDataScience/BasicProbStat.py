import numpy as np

a = np.array([[0,1,2],[2,1,0]])

print(np.mean(a))                   # np.mean(a, axis, dtype, out, keepdims)
print(np.mean(a, axis = 0))         # 평균
print(np.mean(a, axis = 1))         # axis는 평균값을 구하기 위한 축

print(np.var(a))                    # 분산 np.var(~~) -> 상동,  표준편차np.std도 동일
print(np.cov(a, ddof = 0))
print(np.cov(a, ddof = 1))

# 공분산 np.cov(m, y, rowvar, bias, ddof, fweights, aweights)
# row는 variable, column은 observation / y는 추가적인 변수와 관측치
# rowvar 이 False면 변수와 관측지가 반대로 됨
# ddof가 젤 소름인 부분인데, 따로 만지지 않으면 ddof는 1이 되어 불편분산(n-1로 나누기)을 구한다. 이거찾느라 30분썼네
# bias 가 False면 N-1에 의해 normalization 진행, 반대면 N에 의해
# 나머지는 검색해서..
