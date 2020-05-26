nm = input()
cl = input()
print(nm+'的颜色是'+cl)
class fruit():
    def __init__(self,name,color):
        self.name=name
        self.color=color
def print_object(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
Fruit=fruit(nm,cl)
print_object(Fruit)
