# create Walk class with required objects and methods

class Walk:

    def __init__(self, date, time, capacity, dog, id = None):
        self.date = date
        self.time = time
        self.capacity = capacity
        self.head_count = 0
        self.dog = dog
        self.id = id

    def increase_head_count(self):
        if self.head_count < self.capacity:
            self.head_count += 1
        else:
            return "This walk is now full"

    def decrease_head_count(self):
        self.head_count -= 1