
from random import *

#1e9=10^9=10억
#INF를 표현시 1e9 or 987654321로 보통 표기함.
#3.954
print(3954e-3)
print(1e9)
name="곧잘이"
age=4
print(str(name)+"는 4살이고..."+name+"산책을 조아해 얘는 어른인가?"+str(age))
print(2**3)
print(7//3)
#부동소수점의 한계로 비정확하게 나올 수있으니 round 반올림 함수를 활용하자.
#절대값
print(abs(-3))
#제곱
print(pow(2,3))
#최댓값
print(max(5,12))
#최솟값
print(min(4,12))
#반올림
print(round(3.14))
from math import *
#내림
print(floor(4.99))
#올림
print(ceil(3.14))
print("this is random function")
print(randrange(1,46))
day=randint(4,28)


a=0.3+0.6
if round(a,2)==0.9:
    print(True)
else:
    print(False)
print(round(a,2))
#파이썬에서 나누기는 실수형으로 보통 처리한다.
b=7
c=3
#나누기
print(b/c)

#몫
print(b//c)
#거듭제곱
print(b**c)

#리스트 자료형

