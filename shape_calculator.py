class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        horizontal = ''.join(['*' for _ in range(self.width)]) + '\n'
        picture = ''
        for _ in range(self.height):
            picture += horizontal
        return picture
    def get_amount_inside(self, rectangle):
        return int(self.get_area() / rectangle.get_area())


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

    def __str__(self):
        return f'Square(side={self.height})'

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        return self.set_side(width)

    def set_width(self, width):
        return self.set_side(width)  
