class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.doubles = set()

    def book(self, start: int, end: int) -> bool:
        for i, j in self.doubles:
            if start < j and end > i:
                return False

        for i, j in self.events:
            if start < j and end > i:
                overlap = (max(start, i), min(end, j))
                self.doubles.add(overlap)
        self.events.append((start, end))
        return True
