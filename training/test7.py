class mammals:
    def walk(self):
        print('walk')


class dog(mammals):
    def bark(self):
        print('bark')


class cat(mammals):
    def meow(self):
        print('meow')



tom=cat()
tom.meow()
print(tom)

tommy=dog()
tommy.bark()
print(tommy)