possible_paths = 0

def checkPalindrom(arr):
    s = ""
    for x in arr:
        s+=x

    if s == s[::-1]:
        return 1
    else:
        return 0


def findPaths(mat, path, i, j):
    global possible_paths
    (M, N) = (len(mat), len(mat[0]))
 
    # if the last cell is reached, print the route
    if i == M - 1 and j == N - 1:
        #print(path + [mat[i][j]])
        possible_paths += checkPalindrom(path + [mat[i][j]])
        return
 
    # include the current cell in the path
    path.append(mat[i][j])
 
    # move right
    if 0 <= i < M and 0 <= j + 1 < N:
        findPaths(mat, path, i, j + 1)
 
    # move down
    if 0 <= i + 1 < M and 0 <= j < N:
        findPaths(mat, path, i + 1, j)
 
    # backtrack: remove the current cell from the path
    path.pop()
 
 
if __name__ == '__main__':

    n, m = map(int, input().split())
    ls = list(map(str, input().split()))
    mat = []
    j = 0
    for i in range(n):
        mat.append(ls[j:j+m])
        j = j+m

    print(mat)
    path = []
 
    # start from `(0, 0)` cell
    x = y = 0
 
    findPaths(mat, path, x, y)
    print(possible_paths)

'''
3 4
a a a b b a a a a b b a
'''
