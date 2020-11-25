class ExamRoom:

    def __init__(self, N: int):
        self.n = N
        self.seats = []

    def seat(self) -> int:
        if len(self.seats) == 0:
            self.seats.append(0)
            return 0
        else:
            best = None
            for i in range(0, len(self.seats) + 1):
                if i == 0:
                    mid = 0
                    min_diff = self.seats[i]
                elif i == len(self.seats):
                    mid = self.n - 1
                    min_diff = mid - self.seats[i - 1]
                else:
                    diff = self.seats[i] - self.seats[i - 1]
                    mid = self.seats[i - 1] + (diff // 2)
                    min_diff = diff // 2

                if not best or min_diff > best[0]:
                    best = [min_diff, mid, i]
            self.seats.insert(best[2], best[1])
            return best[1]

    def leave(self, p: int) -> None:
        self.seats.remove(p)
