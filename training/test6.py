class person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print('you can talk')

person1 = person('sagar')
person1.talk()
print(person1.name)
person2= person('dalal')
person2.talk()
print(person2.name)

