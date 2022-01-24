# ================================================================
# 问题1:开盲盒:一组n个玩偶,每个盒子等概率放一个,集齐n个期望买多少盒
# 问题2:n种玩偶，第k次购买时，买到新款的概率
# 问题3:n种玩偶，第k次购买时，还有机会买到新款的概率
# 问题4：若玩偶不是等概率出现，求集齐n个期望买多少盒
# ================================================================
# solution1：期望DP
# 状态：dp[i]表示已经有i种玩偶的前提下，集齐n个需要买的盲盒数的期望
# 状态转移：dp[i] = 1(cost) + p(买到新的)*dp[i+1] + p(买到旧的)*dp[i]
# ================================================================
# solution2:几何分布:无后效性&期望
# 定义dp[i]为买到i个不同玩偶则立即停止买盲盒，需要购买的盲盒数的期望
# dp[i] = dp[i-1] + n/(n-i+1)
# ================================================================
# problem2:等价于求第k-1次购买时，买到的玩偶种类的期望
# 定义dp[i]为第i次购买时候买到的玩偶种类的期望
# dp[i] = dp[i-1] + (n-dp[i-1])/n
# return (n-dp[k-1])/n
# ================================================================
# problem3:保留一个玩偶始终不选
# return ((n-1)/n)^k
# ================================================================

import math

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

def problem3(k=5, n=100):
    print(math.pow(((n-1)/n),k))

def number2bin(number,n):
    res = bin(number)[2:]
    res = '0'*(n-len(res)) + res
    return str(res)

def problem4(n=5, prob=[0.1, 0.1, 0.2, 0.2, 0.4]):
    final = pow(2,n) # -1
    dp = [0 for _ in range(final)] # dp[i]表示已经集齐j这种组合的情况下，买够n个玩偶的期望
    dp[-1] = 0
    for i in range(final-2, -1, -1): # 倒序
        dp[i] = 1
        bin = number2bin(i,n)
        nonew = 1
        for index in range(len(bin)):
            if(bin[index]=='0'):
                new = list(bin)
                new[index] = '1'
                new = ''.join(new)
                j = int(new,2)
                dp[i] += prob[index]*dp[j]
                # dp[i] = (1/(1-transfer[i][i]))*(1+∑{新的j, (i转移到j的概率)*dp[j]})
            else:
                nonew -= prob[index]
        dp[i] /= nonew
 
    print(dp[0])
    
solution1()
solution2()
problem2(k=2, n=10)
problem3(k=2, n=10)
problem4(n=5, prob=[0.1, 0.1, 0.2, 0.2, 0.4])