import math


class Solution:
    def visiblePoints(self, points: list, angle: int, location: list) -> int:
        all_degrees = []
        taken_out = 0
        for point in points:
            if point == location:
                taken_out += 1
                continue

            y_diff = point[1] - location[1]
            x_diff = point[0] - location[0]
            degree = math.degrees(math.atan2(y_diff, x_diff))
            all_degrees.append(degree)

        sorted_degrees = sorted(all_degrees)
        sorted_degrees = sorted_degrees * 2
        start, end, max_points = 0, 0, 0
        while start < (len(sorted_degrees) // 2):
            if (sorted_degrees[end] - sorted_degrees[start]) % 360 > angle:
                start += 1
            else:
                max_points = max(max_points, (end - start) + 1)
                if max_points == len(sorted_degrees) // 2:
                    return max_points + taken_out
                end += 1

        return max_points + taken_out
