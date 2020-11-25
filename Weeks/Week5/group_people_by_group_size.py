class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        groups = {}
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = [[]]

            if len(groups[size][-1]) == size:
                groups[size].append([])

            groups[size][-1].append(i)

        result = []
        for group_list in groups.values():
            result += group_list

        return result
