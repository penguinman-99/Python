#리스트 
subway=[10,20,30]
print(subway)
subway=["사당","교대","잠실"]
#해당 원소의 위치 반환
print(subway.index("사당"))
#원소추가
subway.append("시청")
#원소제거
subway.pop()
print(subway)
#원소 사이에 추가하기
subway.insert(1,"신도림")
print(subway)

#중복원소가 몇개인지 확인 
subway.append("신도림")
print(subway.count("신도림"))
#원소들의 정렬
subway.sort()
print(subway)
#원소 뒤집기
subway.reverse()
print(subway)
#리스트 초기화
subway.clear()

#다양한 자료형 삽입 가능
mixlist=["김균호",134,True]


#사전 dictionary

cabinet={3:"후잉",5:"균호"}
print(cabinet[3])
#없는 키를 출력시도시 오류남.
print(cabinet[5])
#get을 이용시 없는 키를 출력시도시 none 반환함.
print(cabinet.get(3))
print(cabinet.get(6,"사용가능"))
#해당 원소가 cabinet에 있는가?
print(3 in cabinet)

ccr={"A-3":"ZZ","B-4":"GG"}
#원소 추가

ccr["C-30"]="HH"
#원소 삭제 
del ccr["C-30"]

#key만 출력
print(ccr.keys())
# value 출력
print(ccr.values())
#초기화 
ccr.clear()

#튜플, 리스트보다 빠르지만 변경이 불가능.
menu=("돈까스","카레까스")
print(menu[0])
profile=("김균호",990727,"C++")
print(profile)


#세트
#중복X, 순서없음
my_set={1,2,3,3,3}
print(my_set)
java={"ㅇㅇ","ㄴㄴ","ㅁㅁ"}
python=set(["ㅇㅇ","ㄴㄴ"])
print(java and python)
print(java.intersection(python))

#합집합
print(java or python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))

python.add("ㅅㅅ")
java.remove("ㄴㄴ")

menu={"커피","주스","우유"}
menu=list(menu)

#Quiz
from random import *

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(list1)
print("치킨 당첨자:%d" %list1[0])
list1.pop(0)
print("커피 당첨자:%d %d %d" %(list1[0],list1[1],list1[2]))

lst=range(1,21)
lst=list(lst)
shuffle(lst)
print(lst)
winners=sample(lst,4)
print("커피:{0}".format(winners[1:]))
print("맥주:{0}".format(winners[0]))