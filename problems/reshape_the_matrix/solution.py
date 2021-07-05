class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) == r and len(mat[0]) == c:
            return mat
        elif len(mat) * len(mat[0]) == r*c:
            nl = [[0] * c for _ in range(r)]
            pi, pj = 0, 0
            #print(nl)
            for i in range(r):
                for j in range(c):
                    print(pi, pj)
                    nl[i][j] = mat[pi][pj]
                    if pj + 1 > len(mat[0]) - 1:
                        pj = 0
                        pi += 1
                    else:
                        pj += 1
            return nl
        else:
            return mat