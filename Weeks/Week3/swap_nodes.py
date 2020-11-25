import os


def swapNodes(indexes, queries):
    results = []
    for q in queries:
        res, stack, depth = [], [(1, 1)], 1
        visited = {1}
        swapped = set()

        while stack:
            current, level = stack.pop()
            ind = current - 1

            if level % q == 0 and current not in swapped:
                indexes[ind] = list(reversed(indexes[ind]))
                swapped.add(current)

            left, right = indexes[ind]
            if left > -1 and left not in visited:
                stack.append((current, level))
                stack.append((left, level + 1))
                visited.add(left)
            else:
                res.append(current)
                if right > -1 and right not in visited:
                    stack.append((right, level + 1))
                    visited.add(right)
        results.append(res)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
