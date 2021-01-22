#temp=int(input("기온?"))

#if temp<=10:
#    print("추웡")
#elif temp>=20 and temp<=40:
#    print("따뜻해")
#else:
#    print("미지근해")
for i in range(60,101):
    print("{0}".format(i))

name=["균호","동현","경빈","무야호"]
for i in name:
    print("{0}님 들어오세요".format(i))

#while
customer="토오르"
index=5
while index>=1:
    print("{0}, 커피 드셔요. {1}번 남음.".format(customer,index))
    index-=1
    if index==0:
        print("커피없서")
   
#customer="아이언맨"
#person="Unknown"
#while person !=customer:
#    print("{0}, 커피 드셔요..".format(customer))
#    person=input("누구임?")
    

#continue, break

absent=[2,5]
no_book=[7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("수업 쫑남")
        break
    else:
        print("{0}번~".format(student))

#출석번호가 1,2,3,4 앞에 100 붙이기

students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)

students=["whooing","groot","fuzzzz"]
students=[len(i) for i in students]
print(students)
from random import *
cnt=1
for i in range(1,51):
    rdn=randrange(5,51)
    if rdn>=5 and rdn<=15:
        print("{0}번째 손님 (소요시간:{1}분)".format(i,rdn))
        cnt+=1
    else:
        print("{0}번째 손님 (소요시간:{1}분)".format(i,rdn))
print(cnt)

