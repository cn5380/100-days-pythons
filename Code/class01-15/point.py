# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
from cmath import sqrt


# 创建一个类，可以描述在平面上的点，有x,y坐标
class Point:
    def __init__(self, x=0, y=0):
        """初始化的坐标
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """新的坐标位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_p(self, dx, dy):
        """移动指定的增量
        :param dx: 横坐标的增量
        :param dy: 纵坐标的增量
        """
        self.x -= dx
        self.y -= dy

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self) -> str:
        return "(%s, %s)" % (str(self.x), str(self.y))


def main():
    point1 = Point(2, 2)
    point2 = Point()
    print(point1)
    print(point2)

    point2.move_to(99, 6)
    print(point2)
    print(point1.distance_to(point2))


if __name__ == "__main__":
    main()
