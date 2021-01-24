name="마린" #이름
hp=40   #체력
dmg=5   #공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1},".format(hp,dmg))

#탱크
tank_name="탱크"
tank_hp=150
tank_dmg=30
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1},".format(tank_hp,tank_dmg))

def attack(name,location,damage):
    print("{0}:{1}로 공격. [공격력 {2}]".format(name,location,damage))

attack(name,"1시",dmg)
attack(tank_name,"1시",tank_dmg)  

class Unit:
    def __init__(self,name,hp,speed):
        #self:멤버변수
        self.name=name
        self.hp=hp
        self.speed=speed
    def move(self,location,speed):
        print("지상 유닛 이동")
        print("{0} {1}방향으로 이동. 속도[{2}]".format(self.name,location,self.speed))

class AttackUnit(Unit):
    def __init__(self,name,hp,speed,damage):
        #self:멤버변수
        Unit.__init__(self,name,hp,speed)
        self.damage=damage
    def attack(self,location):
        print("{0}유닛이 {1}방향으로 공격중. 공격력:{2}".format(self.name,location,self.damage))
    def damaged(self,damage):
        print("{0}유닛이 {1} 데미지를 입음.".format(self.name,self.damage))
        self.hp-=damage
        print("{0}: 현재 체력은 {1}".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}: 사망했습니다.".format(self.name))

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed
    def fly(self,name,location):
        print("{0}:{1}로 날아갑니다 [속도{2}]".format(name,location,self.flying_speed))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        print("공중 유닛 이동")
        self.fly(self.name,location)
vulture=AttackUnit("벌쳐",80,10,20)

battlecruiser=FlyableAttackUnit("배틀크루져",500,25,10)
vulture.move(vulture.name,"11시")
battlecruiser.move("9시")
