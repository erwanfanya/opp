class Robot:
    def __init__(self, name, color, job):
        self.name = name
        self.color = color
        self.job = job

    def introduce(self):
        print("Hello! I am a robot.")
        print("My name is", self.name)
        print("My color is", self.color)
        print("My job is", self.job)

    def say_hello(self):
        print("Nice to meet you!")



robot1 = Robot("Robo", "Blue", "Helping people")

robot1.introduce()
robot1.say_hello()