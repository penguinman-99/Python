
a=[1,4,3]
print("기본리스트",a)
#원소 삽입

a.append(2)
print("삽입한 리스트", a)

a.sort()    
print("오름차순 리스트", a)

a.sort(reverse=True)
print("내림차순 리스트", a)

a.reverse()
print("원소 뒤집기", a)
#insert,remove: O(N)이므로 시간초과 유의할것.

a.insert(2,3)
print("배열 위치 2에 3추가", a)

a.remove(1)
print("값이 1인 데이터 삭제", a)

remove_set={3,5}

result=[i for i in a if i not in remove_set]

print(result)
