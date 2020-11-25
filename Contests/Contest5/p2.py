class Solution:
    def alertNames(self, keyName: list, keyTime: list) -> list:
        sorted_times = sorted(zip(keyTime, keyName))
        found = {}

        results = set()
        for time_string, name in sorted_times:
            h, m = time_string.split(":")
            time = int(h) * 60 + int(m)

            if name not in found:
                found[name] = {(1, time)}
            else:
                addables = {(1, time)}
                removables = set()
                for el in found[name]:
                    if time - el[1] > 60:
                        removables.add(el)
                    elif el[0] == 1:
                        removables.add(el)
                        addables.add((2, el[1]))
                    else:
                        results.add(name)
                        removables.add(el)
                for i in removables:
                    found[name].remove(i)
                for i in addables:
                    found[name].add(i)
        return sorted(results)
