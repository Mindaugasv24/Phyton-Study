
print('--------------------------Lesson: class methods------------------------')


class Rectangle:
    """r"""
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """r"""
        return self.width * self.height

    @classmethod
    def from_square(cls, side_length: float) -> "Rectangle":
        """r"""
        return cls(side_length, side_length)


rectangle1: Rectangle = Rectangle(3.0, 4.0)
rectangle2: Rectangle = Rectangle.from_square(2.0)

print(rectangle1.area())  # 12.0
print(rectangle2.area())  # 4.0

# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     @classmethod
#     def create_object_from_data(cls, x, y):
#         return cls(x, y)


# rectangle1 = Rectangle(3.0, 4.0)
# rectangle2 = Rectangle.create_object_from_data(3.0, 4)

# print(rectangle1.area())  # 12.0
# print(rectangle2.area())  # 4.0
