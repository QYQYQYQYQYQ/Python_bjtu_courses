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

People1 = people("孙悟空",50,"金箍棒",20)
People2 = people("猪八戒",100,"九钉耙",15)
People3 = people("沙僧",75,"降妖宝杖",10)

def print_object(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

print_object(People1)
print_object(People2)
print_object(People3)

print(peopleNum)