
class Rhombus:
    def __init__(self, side_a, angle_a, angle_b=None):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b


    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Сторона повинна бути > 0")

        if name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Кут a має бути в межах (0, 180)")
            super().__setattr__("angle_b", 180 - value)

        if name == "angle_b":
            return

        super().__setattr__(name, value)


r = Rhombus(5, 70)

print(r.side_a)
print(r.angle_a)
print(r.angle_b)