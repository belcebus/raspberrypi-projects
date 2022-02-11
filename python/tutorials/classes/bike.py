from time import strftime


class Bike:

    
    def __init__(self, colour: str, frame_material: str):
        self.colour=colour
        self.frame_material=frame_material

    def brake(self):
        print("Braking!")


red_bike=Bike("red",3)
blue_bike=Bike("blue","steel")

print(f"Red bike colour: {red_bike.colour}")
print(f"Blue bike colour: {blue_bike.colour}")

red_bike.brake()
blue_bike.brake()
