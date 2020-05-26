peopleNum=0
class people():
    def __init__(self, name, life, weaponName, weaponPower):
        global peopleNum
        self.name=name
        self.life=life
        self.weaponName=weaponName
        self.weaponPower=weaponPower
        peopleNum+=1
        self.peopleAlive=True
    def showResult(self, attacker_name, attacker_weaponname):
        if self.life<=0:
            print(attacker_name+'用'+attacker_weaponname+'攻击了'+self.name+' '+self.name+'阵亡了')
        else:
            print(attacker_name+'用'+attacker_weaponname+'攻击了'+self.name+' '+self.name+'剩余血量',end="")
            print(self.life)
    def beAttacked(self, attacker_weaponpower, attacker_name, attacker_weaponname):
        self.life-=attacker_weaponpower
        self.showResult(attacker_name,attacker_weaponname)
life1 = eval(input())
life2 = eval(input())
life3 = eval(input())
People1 = people("孙悟空",life1,"金箍棒",20)
People2 = people("猪八戒",life2,"九钉耙",15)
People3 = people("沙僧",life3,"降妖宝杖",10)
People2.beAttacked(People1.weaponPower,People1.name,People1.weaponName)
if People2.life>0:
    People3.beAttacked(People2.weaponPower,People2.name,People2.weaponName)
if People3.life>0:
    People1.beAttacked(People3.weaponPower,People3.name,People3.weaponName)
