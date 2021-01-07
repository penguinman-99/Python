
#1e9=10^9=10억
#INF를 표현시 1e9 or 987654321로 보통 표기함.
#3.954
print(3954e-3)
print(1e9)

#부동소수점의 한계로 비정확하게 나올 수있으니 round 반올림 함수를 활용하자.

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

