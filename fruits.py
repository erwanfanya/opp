class Fruits:
    taste = "sweet"

    def __init__(self,name,color):
        self.name = name
        self.color = color

apple = Fruits('apple', 'Red')
banana = Fruits('Banana', 'Yellow')

print(apple.taste)
print(apple.name,apple.color)
print(banana.name, banana.color)
