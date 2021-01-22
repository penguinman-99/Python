def open_account():
    print("새 계좌 생성")
#입금
def deposit(balance,money):
    print("입금 끝. 잔액은 {0}원.".format(balance+money))
    return balance+money

def withdraw(balance,money): #출금
    if(money<balance):
        print("출금끝.. {0}".format(balance-money))
        return balance-money
    else:
        print("출금이 안되요...")
def withdraw_night(balance,money): #저녁 출금
    fee=500
    return fee, balance-money-fee

balance=0
balance=deposit(balance,1000)

commission,balance=withdraw_night(balance,500)
print("수수료 {0}원, 잔액은 {1}원".format(commission,balance))

#함수의 기본값

#def profile(name,age=17,main_lang="파이썬"):
#    print("이름:{0}, 나이:{1}, 주언어:{2}".\
#        format(name,age,main_lang))

#profile("김균호")

#가변인자
def profile(name,age,*lang):
    print("이름: {0}\t나이:{1}\t".format(name,age),end=" ")
    for i in lang:
        print(i,end=" ")
    print()

profile("규노",33,"C++","파이썬")
print("교수님",55,"C++","파이썬","자바","스위프트")

gun=10
def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print("함수 내 총:{0}".format(gun))
    return gun

gun=checkpoint_ret(gun,2)

def aver_weight(height,gender):
    if(gender=="남자"):
        return (height/100)**2*22
    elif(gender=="여자"):
        return (height/100)**2*21
    else:
        return 0
height=175
gender="남자"
print("키 {0}의 {1} 표준 체중은 {2}입니다.".format(height,gender,round(aver_weight(height,gender),2)))

