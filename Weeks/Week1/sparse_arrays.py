import os


def matchingStrings(strings, queries):
    collection, results = {}, []
    for string in strings:
        if string in collection:
            collection[string] += 1
        else:
            collection[string] = 1
    for query in queries:
        if query in collection:
            results.append(collection[query])
        else:
            results.append(0)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
