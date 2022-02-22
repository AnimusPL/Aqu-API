import time

class World:
    def __init__(self):
        print("World is in progress...")
        user_interface = UI()
        aquarium = Aquarium()

class UI:
    def __init__(self):
        pass

class Aquarium:
    def __init__(self):
        self.width = 0
        self.height = 0
        fishes = [Fish() for fishes in range(10)]
        print("Aquarium has been created")
        print(fishes)

class Fish:
    def __init__(self):
        self.ID = 0
        self.position_x = 0
        self.position_y = 0
        self.move_direction_x = 0
        self.move_direction_y = 0
        self.hungry_level = 0
    
    def move(self):
        pass

    def get_hungry():
        pass

num = 1

def update(num):
    while True:
        time.sleep(0.5) #only for testing purposes
        print(num)


if __name__ == "__main__":
    world = World()