class Figure:
    unit = "cm"

    def _init_(self):
        pass

    def calculate_area(self):
       pass

    def info(self):
       pass


class Circle(Figure):
    def _init_(self, radius):
        super()._init_()
        self.__radius = radius

    def calculate_area(self):
        return 3.14159 * self.__radius ** 2

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area():.2f}{self.unit}².")


class RightTriangle(Figure):
    def _init_(self, side_a, side_b):
        super()._init_()
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return 0.5 * self._side_a * self._side_b

    def info(self):
        print(f"RightTriangle side a: {self._side_a}{self.unit}, side b: {self._side_b}{self.unit}, area: {self.calculate_area():.2f}{self.unit}².")


circle1 = Circle(2)
circle2 = Circle(3)

triangle1 = RightTriangle(5, 8)
triangle2 = RightTriangle(3, 4)
triangle3 = RightTriangle(6, 7)

figures = [circle1, circle2, triangle1, triangle2, triangle3]

for figure in figures:
    figure.info()