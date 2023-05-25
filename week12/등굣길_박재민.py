def solution(m, n, puddles):
    memo = [[0] * (m + 1) for _ in range(n + 1)]
    memo[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or [j, i] in puddles:
                continue
            memo[i][j] = memo[i][j - 1] + memo[i - 1][j]

    return memo[n][m] % 1000000007
