# ================================================================
# 开盲盒:一组n个玩偶,每个盒子等概率放一个,集齐n个期望买多少盒
# ================================================================
# solution1：期望DP
# 状态：dp[i]表示已经有i种玩偶的前提下，集齐n个需要买的盲盒数的期望
# 状态转移：dp[i] = 1(cost) + p(买到新的)*dp[i+1] + p(买到旧的)*dp[i]
# 起点: dp[n]=0, 终点:dp[0]=?
# ================================================================
# solution2:几何分布(几何分布的无后效性、几何分布期望为1/p)
# 定义dp[i]为买到i个不同玩偶则立即停止买盲盒，需要购买的盲盒数的期望
# dp[i] = dp[i-1] + n/(n-i+1)
# ================================================================
# 衍生题目：n种玩偶，第k次购买时，还有机会买到新款的概率
# 等价于求第k-1次购买时，买到的玩偶种类的期望
# 定义dp[i]为第i次购买时候买到的玩偶种类
# dp[i] = dp[i-1] + (n-dp[i-1])/n
# ================================================================

def solution1(n = 100):
    dp = [0 for _ in range(n+1)] # dp[i]表示已经有i种玩偶的前提下，集齐n个需要买的盲盒数的期望
    dp[n] = 0.0
    for i in range(n-1, -1, -1):
        dp[i] = dp[i+1] + (n/(n-i))
        # print(i, dp[i])
        
    print(dp[0])

def solution2(n=100):
    dp = [0 for _ in range(n+1)]
    dp[0] =0.0
    for i in range(1,n+1):
        dp[i] = dp[i-1] + n/(n-i+1)
    print(dp[n])
    
def problem2(k=5 ,n=100): # 共n个玩偶，第k次购买
    dp = [0 for _ in range(k)]
    dp[0] = 0.0
    for i in range(1,k):
        dp[i] = ((n-1)/n)*dp[i-1] + 1
    print((n-dp[k-1])/n)

solution1()
solution2()
problem2()