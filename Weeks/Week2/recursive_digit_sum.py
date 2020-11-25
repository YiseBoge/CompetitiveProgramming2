import os


def superDigit(n, k):
    number = str(n)
    if len(number) == 1:
        return number
    added = 0
    for i in number:
        added += int(i)
    new = added * k
    return superDigit(new, 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
