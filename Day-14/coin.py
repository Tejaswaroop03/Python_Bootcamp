def possible(coins,target):
    dp=[False]*(target + 1)
    dp[0]=True   
    for i in coins:
        for j in range(i,target + 1):
            if dp[j-i]:
                dp[j]=True
    return dp[target]

coins=[5,10,25]
target=6
print(possible(coins,target))