def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0]:
        return 0
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0]*n for _ in range(m)]
    if obstacleGrid[0][0] == 0:
        dp[0][0] = 1
    else:
        return 0
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    print (dp)
    print(dp[-1][-1])

#uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,1,0]])
