# 상속, 다형성

class Animal:
    def __init__(self, n):
        self.name = n

    def speak(self):
        return "소리를 냅니다"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name}가 멍멍 소리를 냅니다"

class Cat(Animal):
    def __init__(self, n, c):
        super().__init__(n)
        self.color = c
    def speak(self):
        return f"{self.color}고양이 {self.name}가 야옹 소리를 냅니다"
    
dog = Dog("초코")
print(dog.speak())

cat = Cat("나비","검정색")
print(cat.speak())