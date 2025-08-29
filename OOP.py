# Assignment 1: Design Your Own Class 🏗️

class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    # Method to display phone details
    def show_details(self):
        print(f"📱 {self.brand} {self.model} with {self.storage}GB storage.")

    # Method to simulate making a call
    def make_call(self, number):
        print(f"📞 Calling {number} from {self.model}...")

# Inheritance: Smartphone5G extends Smartphone
class Smartphone5G(Smartphone):
    def __init__(self, brand, model, storage, network_speed):
        # Call parent constructor
        super().__init__(brand, model, storage)
        self.network_speed = network_speed

    # Method specific to Smartphone5G
    def browse_internet(self):
        print(f"🌐 Browsing at {self.network_speed} Mbps on {self.model}.")

# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone2 = Smartphone5G("Apple", "iPhone 14 Pro", 256, 1000)

phone1.show_details()
phone1.make_call("0712345678")

phone2.show_details()
phone2.make_call("0798765432")
phone2.browse_internet()



# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        pass  # Base method (to be overridden by subclasses)

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Polymorphism in action!
