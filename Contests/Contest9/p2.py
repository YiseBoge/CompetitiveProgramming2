import math


class Solution:
    def bestCoordinate(self, towers: list, radius: int) -> list:
        def distance(tw, pt):
            return math.sqrt((tw[0] - pt[0]) ** 2 + (tw[1] - pt[1]) ** 2)

        def signal(tw, pt):
            d = distance(tw, pt)
            return math.floor(tw[2] / (1 + d))

        points = set()
        for tower in towers:
            for i in range(tower[0] - radius, tower[0] + radius + 1):
                for j in range(tower[1] - radius, tower[1] + radius + 1):
                    point = (i, j)
                    if i >= 0 and j >= 0 and distance(tower, point) <= radius:
                        points.add(point)

        best = [0, 0, 0]
        for point in sorted(points):
            strength = 0
            for tower in towers:
                if distance(tower, point) <= radius:
                    strength += signal(tower, point)

            if strength > best[2]:
                best = point + (strength,)

        return best[:2]
