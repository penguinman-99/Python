my_addr="990727-1234567"
print(my_addr[:6])
sex="Null"
if my_addr[7]==str(1):
    sex="male"
else:
    sex="female"
print("년도:"+str(my_addr[:2]))
print("성별:"+str(sex))
print("월:"+my_addr[2:4])#2부터 4 '직전' 까지 
print("일:"+my_addr[4:6])
#문자열 처리함수

py="Python is Amazing"
#모든 문자열을 대, 소문자로 출력
print(py.upper())
print(py.lower())
#해당 문자가 대문자인가?
print(py[0].isupper())
#문자열 길이
print(len(py))
#해당 문자열 대체
print(py.replace("Python","C++"))
#해당 문자가 위치해있는 곳, 단 찾을 수 없다면 오류 
index=py.index("n")
print(index)
#그 다음 위치부터 찾을 수 있음
index=py.index("n",index+1)
#index와 유사함. 단, 찾을 수 없다면 -1를 반환
print(py.find("n"))
#n이 몇번 나오는가?
print(py.count("n"))


#문자열 포맷
# %d: 정수, %s: 문자열 %c: 한글자
print("I'm %d years old." %20)
print("I love %s" %"C++")
print("apple is starting alphabet %c" %"A")
print("I love %s and %s." %("김치","탕수육"))

#Second
print("I'm {} years old.".format(20))
print("I also love {0} and {1}.".format("coffe","kimchi"))
print("but i hate {1} and {0}.".format("oyster","cheese"))

#Third
print("Wow! {language} is Amzaing!".format(language="python"))

#Final. but only upper 3.6 version is avaliable
color="red"
food="oyster"
print(f"ah, what is the {color} {food}?")


#탈출문자
#\n: 줄바꿈

print("옛말에 백문이 \n불여일견이거늘...")

# "를 쓰고 싶다면 앞에 \ 
print("제 이름은 \"공혁준\" 입니다")

# \\: 문장 내에선 \로 바꿈

print("돈 1000\\내놔")

# \r: 커서를 맨 앞으로 이동.
print("red apple\rkimchi")

# \b: 백스페이스(한글자 지우기)
# \t: 탭키

#Quiz:
url="http://youtube.com"
str1=url.replace("http://","")
str2=str1.find(".")
str3=str1[:str2]
print(str3)
password=str3[:3]+str(len(str3))+str(str3.count("e"))+"!"
print(password)