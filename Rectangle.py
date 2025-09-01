# Name: Ka Yan Dreibelbis
# Course: CIS261
# Week 6 - Rectangle Calculator

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                print("*", end=" ")
            print()


def main():
    print("Rectangle Calculator")
    again = "y"
    while again.lower() == "y":
        height = int(input("Height: "))
        width = int(input("Width: "))

        rect = Rectangle(height, width)

        print("Height:", rect.height)
        print("Width:", rect.width)
        print("Perimeter:", rect.perimeter())
        print("Area:", rect.area())
        rect.draw()

        again = input("Continue? (y/n): ")


main()
