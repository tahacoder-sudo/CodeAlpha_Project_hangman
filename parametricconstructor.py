class Person:
    def __init__(self,n,o):
        print("Hey i am a student")
        self.name=n
        self.occupation=o
    def info(self):
        print(f"{self.name} is a {self.occupation}")



a=Person("taha","student")
b=Person("bilal","student")
a.info()
































