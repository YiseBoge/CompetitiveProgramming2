import math


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def within_circle(point):
            nonlocal radius, x_center, y_center
            x, y = point
            return math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) <= radius

        def within_rectangle(point):
            nonlocal x1, y1, x2, y2
            x, y = point
            return x1 <= x <= x2 and y1 <= y <= y2

        rectangle_corners = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
        circle_edges = [
            (x_center + radius, y_center),
            (x_center - radius, y_center),
            (x_center, y_center + radius),
            (x_center, y_center - radius)
        ]

        print(rectangle_corners, circle_edges)
        for corner in rectangle_corners:
            if within_circle(corner):
                return True
        for edge in circle_edges:
            if within_rectangle(edge):
                return True

        if x_center - radius <= x1 < x2 <= x_center + radius and y1 <= y_center <= y2:
            return True
        if y_center - radius <= y1 < y2 <= y_center + radius and x1 <= x_center <= x2:
            return True

        return False
