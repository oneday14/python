# f_read_txt 사용자 정의함수를 사용하여 emp.csv 파일을 읽고 다음을 수행
from my_func import *
L1 = f_read_txt('emp.csv',sep=',', fmt=str)

L2 = L1[1:]

# 1) 이름을 모두 소문자로 저장
li1 = [[1,2,3],[10,20,30]]
li1[0][0]
li1[1][0]

f1 = lambda x : x[0]
list(map(f1,li1))

# 이름 값 추출
f1 = lambda x : x[1]
ename = list(map(f1,L2))

'A'.lower()

[ x.lower() for x in ename ]

# 2) 입사년도 추출
f1 = lambda x : x[4]
hdate = list(map(f1,L2))

'1981/09/08 00:00:00'[:4]

[x[:4] for x in hdate]

# 3) 10% 인상된 연봉 계산
f1 = lambda x : x[5]
sal = list(map(f1,L2))

int('1100') * 1.1

[int(x) * 1.1 for x in sal]

# 4) comm이 없는 직원은 100 부여
f1 = lambda x : x[-2]
comm = list(map(f1,L2))

[ 100 if x=='' else int(x) for x in comm ]

########## 여기까지는 복습입니다. ##########

# =============================================================================
# 자료구조
# 1. 리스트
# 2. 튜플
# 3. 딕셔너리
# 4. 세트
# 5. 배열
# 6. 데이터프레임
# =============================================================================

# 배열(array)
# - 다차원 가능
# - 서로 같은 데이터 타입 허용
# - numpy 모듈 호출 후 사용

import numpy as np

# 1. 생성
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l1[0,0]

a1 = np.array(l1)
type(a1)

# 2. 색인
a1[0,0]
a1[0,:]  # 첫번째 행 선택
a1[:,0]  # 첫번째 컬럼 선택

a1[[0,2], :]   # 리스트 색인 가능(행 선택)

a1[0:2,:]      # 슬라이스 색인 가능

a1[1:3,1:3]        # 행, 열 모두 슬라이스 색인 가능
a1[[1,2],[1,2]]    # 행, 열 모두 리스트 색인 시 point indexing으로 해석
                   # => p(1,1) , p(2,2)

a1[a1[:,1] > 5, :] # boolean indexing 가능
a1[a1 > 5]

# 3. 배열 메서드
a1.dtype           # 배열을 구성하는 데이터 타입
a1.ndim            # 차원의 수
a1.shape           # 모양

np.arange(1,10).reshape(3,3)

# 4. 연산
a2 = np.arange(10,100,10).reshape(3,3)
a3 = np.arange(10,130,10).reshape(4,3)

a1 * 9             # 스칼라 연산 가능
a1 + a2            # 서로 같은 크기를 갖는 배열끼리 연산 가능
a1 + a3            # 서로 다른 크기를 갖는 배열끼리 기본적으로 연산 불가

# 5. 배열의 broadcast 기능
# - 서로 다른 크기의 배열 연산 시 크기가 작은 배열의 반복 전달을 가능하게 하는 연산
# - broadcast 전제 조건 필요
# 1) 큰 배열이 작은 배열의 배수 형태
# 2) 작은 배열의 행, 컬럼 중 1의 크기를 가지고 있는 형태

a1 + np.array([10,20,30])   # (3X3) (1X3)
a1 + np.array([10,20,30]).reshape(3,1)   # (3X3) (3X1)

a4 = np.arange(1,17).reshape(4,4)
a5 = np.arange(10,90,10).reshape(2,4)

a4 + a5

# 예제) a1 배열에서 1,3,7,9 추출
a1[c(1,3),c(1,3)]
a1[[0,2],[0,2]]       # 불가

a1[[0,2],:][:,[0,2]]     # 중첩색인으로 가능
a1[np.ix_([0,2],[0,2])]  # np.ix_ 함수로 가능

# [ 연습 문제 ]
# emp 배열에서
emp1 = emp[1:, :]

# 1) sal이 3000이상인 행 선택
emp1[:,-3] >= 3000            # 문자 타입에 대소비교 불가
int(emp1[:,-3])               # int 형 변환함수로 전체 치환 불가
[int(x) for x in emp1[:,-3]]  # list comprehension으로 형 변환 처리

vbool = np.array([int(x) for x in emp1[:,-3]]) >= 3000
emp1[vbool, :]


# 2) comm이 없는 직원의 이름, 부서번호, comm 선택
emp1[emp1[:,-2] == '', :][:,[1,-1,-2]]
emp1[np.ix_(emp1[:,-2] == '',[1,-1,-2])]

# 3) 이름이 S로 시작하는 직원의 이름, 사번, sal 선택
vbool2 = [ x.startswith('S') or x.startswith('s') for x in emp1[:,1]]

emp1[vbool2, :][:,[1,0,-3]]
emp1[np.ix_(vbool2,[1,0,-3])]


# [ 연습 문제 ]
# 1. 2부터 시작하는 짝수로 구성된 4X4 배열을 만들고
arr1 = np.arange(2,33,2).reshape(4,4)

# 2. 위 배열에 배열의 첫번째 행을 더한 값 출력
arr1 + arr1[0,:]

# 3. 위 배열에 배열의 첫번째 컬럼을 더한 값 출력
arr1 + arr1[:,0:1]
arr1 + arr1[:,0].reshape(4,1)


# [ 예제 : 다차원 배열 생성 ]
arr2 = np.arange(1,25).reshape(2,3,4)  # 2(층) X 3(행) X 4(열)
arr2[:,0,:]
arr2[:,0:1,:]
arr2[0,[1,2],2]

# [ 연습 문제 ]
L1   = [[1,2,3],[4,5,6],[7,8,9]]
arr1 = np.array(L1)
arr2 = np.arange(1,25).reshape(2,3,4)

# 1. arr1에서 5,6,8,9 추출
arr1[1:3,1:3]
arr1[1:3,[1,2]]
arr1[[1,2],:][:,[1,2]]
arr1[np.ix_([1,2],[1,2])]

# 2. arr1에서 4,7 추출
arr1[[1,2],0]    # 1차원 리턴
arr1[[1,2],0:1]  # 2차원 리턴

# 3. arr2에서 2,3,6,7,14,15,18,19 출력
arr2[:,0:2,1:3]
arr2[:,[0,1],[1,2]]             # point indexing
arr2[:,[0,1],:][:,:,[1,2]]      # 순차적 색인
arr2[np.ix_(:,[0,1],[1,2])]     # : 사용 불가
arr2[np.ix_([0,1],[0,1],[1,2])] # 정수 리스트 형식으로만 가능

# 4. arr2에서 6,7,8 출력
arr2[0,1,[1,2,3]]
arr2[0,1,1:4]
arr2[0:1,1:2,1:4]

# =============================================================================
# emp.csv 파일을 리스트로 불러온 후 배열로 변경
# emp = np.array(L1)
# ename = emp[1:,1]
# sal = emp[1:,-3]
# =============================================================================


# =============================================================================
# R, Python 적용함수 비교
#                          R             Python
# 1차원 원소별 적용       sapply         map(), .map() 
# 2차원 행,열별 적용      apply            .apply
# 2차원 원소별 적용       apply           .applymap
# =============================================================================

