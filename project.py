class Robot:
    def __init__(self, name, model, purpose):
        self.name = name
        self.model = model
        self.purpose = purpose

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.model} model robot.")
        print(f"My purpose is {self.purpose}.")

    def perform_task(self):
        print(f"{self.name} is now performing its task: {self.purpose}.")

my_robot = Robot("Zeno", "XR-500", "assisting humans with daily tasks")

my_robot.introduce()

my_robot.perform_task()
