class Point():
    def __init__(self, input1, input2):#input1 and input2 are x and y
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)
people=["Harry","Ron","Hermione","Ginny"]
for person in people:
    success = flight.add_passanger(person)
    if success:
        print(f"added {person} to the flight successfully.")
    else:
        print(f"No available seats for {person}")