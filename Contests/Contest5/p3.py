class Solution:
    def restoreMatrix(self, rowSum: list, colSum: list) -> list:
        result = []
        for i in range(len(rowSum)):
            res = []
            for j in range(len(colSum)):
                val = min(rowSum[i], colSum[j])
                res.append(val)
                rowSum[i] -= val
                colSum[j] -= val
            result.append(res)
        return result
