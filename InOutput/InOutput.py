
#sep: , 사이에 텍스트 삽입, end: 문장의 끝부분을 해당 텍스트로 대체
#= 개행안됨
import sys
#print("Python", "java","javascript",sys.stdout)
#print("Python", "java","javascript",file=sys.stderr)
scores={"수학":0,"영어":50,"코딩":100}
for subject,score in scores.items():
    #print(subject,score)
    #ljust: 공간확보. 
    print(subject.ljust(8),str(score).rjust(4),sep=":")

#은행 대기순번표
#001을 붙이는 방법? zfill.
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3))

#answer=input("아무 값이나 넣으랜다")
##해당 변수의 타입
#print(type(answer))
#print("입력한건 {0}~".format(answer))

#빈자리는 빈공간으로 두고 오른쪽 정렬을 하되, 총 10자리 공간을 확보

print("{0: >10}".format(500))

#양수일땐 +, 음수일땐 -로 표시 ex:주식?
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
#왼쪽 정렬, 빈칸을 _로 채우기
print("{0:-<+10}".format(500))
#큰 숫자가 들어올때, 세자리마다 콤마를 찍어주기
print("{0:+,}".format(100000000))
#3자리 콤마찍기, 부호도 붙이고, 자릿수도, 빈자리는 *
print("{0:^<+30,}".format(10003434000))
#소수점 출력
print("{0:f}".format(5/3))
#특정 자릿수까지 
print("{0:.3f}".format(5/3))

#파일입출력

#score_file=open("score.txt","a",encoding="utf8")
#score_file.write("w:새로 쓰기 \na:기존 있던내용+추가 내용")
#score_file.close()

score_file=open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

#score_file=open("score.txt","r",encoding="utf8")
##한줄씩만 읽기
#print(score_file.readline())
#print(score_file.readline())
#print(score_file.readline())
#print(score_file.readline())
#score_file.close()



score_file=open("score.txt","r",encoding="utf8")
while True:
    line=score_file.readline()
    if not line:
        break
    print(line,end="") 
score_file.close()
score_file=open("score.txt","r",encoding="utf8")

#lines=score_file.readlines() list 형태로 저장
lines=score_file.readlines()
for i in lines:
    print(i,end="")
score_file.close()


# Pickle

import pickle 
profile_file=open("profile.pickle","wb")
profile={"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile,profile_file)#프로필에 있는 정보를 파일에 저장
profile_file.close()

#피클 데이터를 가지고오자.

profile_file=open("profile.pickle","rb")
profile=pickle.load(profile_file) #파일에 있는 정보를 프로필에 가져옴
print(profile)
profile_file.close()

#with

with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("이렇게 글을 쓰면 된답니다.")

study_file.close()

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8".format(i)) as project:
        project.write("{0}주차 주간보고".format(i))
        project.write("부서:\n")
        project.write("이름:\n")
        project.write("업무요약:\n")
