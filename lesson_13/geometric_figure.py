class Rhombus:
    def __init__(self, side_a, corner_a):
        self.side_a = side_a
        self.corner_a = corner_a  # встановиться і автоматично порахується corner_b

    def __setattr__(self, key, value):
        if key == "side_a":
            if value <= 0:
                raise ValueError("Side 'a' must be greater than 0")
        elif key == "corner_a":
            if not (0 < value < 180):
                raise ValueError("Corner 'a' must be between 0 and 180 degrees")
            # автоматично обчислюємо angle_b
            object.__setattr__(self, "corner_b", 180 - value)

        object.__setattr__(self, key, value)

    def __repr__(self):
        return f"Rhombus(side_a={self.side_a}, corner_a={self.corner_a}, corner_b={self.corner_b})"


r = Rhombus(5, 60)
print(r)
