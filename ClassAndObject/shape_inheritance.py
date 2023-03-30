class Shape:
    def __init__(self, x, y, color):
        self.x = x  # 도형 시작점 x좌표
        self.y = y  # 도형 시작점 y좌표
        self.color = color  # 도형 색상

    def set_color(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)  # 부모 클래스의 생성자 호출
        self.width = width  # 사각형의 너비
        self.height = height  # 사각형의 높이

    def draw(self):
        print(f"Drawing a rectangle at ({self.x}, {self.y}), width={self.width}, height={self.height}, color={self.color}")

class Circle(Shape):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle at ({self.x}, {self.y}), radius={self.radius}, color={self.color}")
