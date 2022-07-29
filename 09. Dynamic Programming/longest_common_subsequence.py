

def longest_common_subsequence(a, b):
    grid = [[0] * len(b) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                grid[i][j] = grid[i-1][j-1]
            else:
                grid[i][j] = max(grid[i-1][j], grid[i][j-1])

    return grid


print(longest_common_subsequence('fish', 'fosh'))
