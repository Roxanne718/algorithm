# ===============================================================
# 古埃及数学的分数表示十分特殊，不允许分子不为 1 的分数存在，
# 比如 2/3 在古埃及数学中只能表示为 1/2 + 1/6
# 请设计算法，对给定的真分数 a/b，请计算出满足以下条件的埃及分数表示：
# 1. 和式中的分数互不相同；
# 2. 和式中的分数个数最少；
# 3. 满足条件 2 的情况下，保留和式中最小分数最大的解。
# 例如，19/45 = 1/5 + 1/6 + 1/18
# ===============================================================
# 思路:
# 为了找最优解，应该做BFS,从(1/c)<=(a/b)的第一个数开始搜索，
# 即 c=ceil(b/a), 但BFS的宽度是无限的
# 若使用DFS，又找不到最优解  ==> 采用IDDFS（迭代加深搜索）
# 每次指定搜索深度，对于每一个搜索深度，总存在一个值d，当c大等于d时，
# 埃及分数和小于当前a/b,故宽度不必再扩展
# ===============================================================
# run with python EgyptFraction.py
# ===============================================================
import math
import copy
BEST = []

# return a/b - 1/c
def sub(a,b,c):
    if b==c:
        aa = a-1
        bb = b
    else:
        aa = a*c-b
        bb = b*c
    for i in range(int(aa), 1, -1):# 约分
        if(aa%i==0 and bb%i==0):
            aa/=i
            bb/=i
    return aa,bb

def iddfs(a, b, depth, res=[])->bool:
    if(a==0):
        global BEST
        if(len(BEST)==0 or len(BEST)>len(res)):
            BEST = res
        elif(len(BEST)==len(res) and BEST[-1]>res[-1]):
            BEST = res
        return True
    elif(depth==0): # max depth
        return False
    begin = math.ceil(b/a)
    flag = False
    while True: # BFS
        if(((1.0/begin)*depth) < (float(a)/float(b))):
            break # 当前深度下没有新的解
        if begin not in res:
            new_a, new_b = sub(a, b, begin)
            tmp_res = copy.deepcopy(res)
            res.append(begin)
            if(iddfs(new_a, new_b, depth-1, res)):
                flag = True
            res = tmp_res
        begin+=1
    return flag

a = 19
b = 45

for depth in range(4):
    BEST.clear()
    if(iddfs(a, b, depth)):
        print(BEST)
        break
    print(f'Depth {depth}:no resolve',flush=True)
