import numpy as np

print(np.pi)                                            # pi 출력 위해서는 numpy 필요


array0 = np.array([[1,0], [-1,1]])
print(array0)                                           # 행렬 출력
print(np.linalg.det(array0))                            # determinent, 행렬식
print(np.linalg.inv(array0))                            # inverse matrix, 역행렬


array1 = np.array([[1,1], [1,0], [0,1]])                # col = 2, row = 3인 matrix
print(array1)
print(array1.T)                                         # transpose


array1_ = np.array([[1,1,0], [1,0,1]])                  # 행렬을 column 기준으로 표현하려면 array1_처럼 하고
print(array1_.T)                                        # transpose 시키는 것이 나을까..?
Rank1_ = np.linalg.matrix_rank(array1_.T)
print(Rank1_)                                           # array1_.T의 Rank는 2
array1_ = np.vstack([array1_,[2,1,1]])                  # 수직으로 새로운 column 쌓기
print(array1_.T)
Rank1_ = np.linalg.matrix_rank(array1_.T)               # 새로운 column(벡터)를 추가해도 array1_.T의 Rank는 2
print(Rank1_)                                           # 2,1,1 은 1,1,0과 1,0,1 에 선형종속이기 때문이다.


array2 = np.array([[2], [3]])
print(array1 @ array2)                                  # matrix multiplication
array3 = np.dot(array1, array2)
print(array3)                                           # matrix multipliation, @ is preferred


data = np.array([[60,5.5,1], [65,5.0,0], [55,6.0,1]])   # 수명을 예상하기 위한 데이터
lifespan = np.array([[66], [74], [78]])                 # 수명
vector_x = np.linalg.solve(data, lifespan)              # 모델 벡터는 data가 linear independent 할 때 unique solution을 가지며
print(vector_x)                                         # Ax = b계산은 np.linalg.solve(A,b)로 할 수 있다.

eig = np.linalg.eig                                     # eigenvalue, eigenvector 출력 방법
print(eig(array0))
eigvalue , eigvector = eig(array0)
print(eigvalue)
print(eigvector)
