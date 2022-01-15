# ==============================================================
# 有一个 n × n 的灯阵，每个灯上均有一个开关，
# 每次拨动开关会使当前灯和相邻灯的开关状态改变。
# 请设计算法，判断给出某种开关图案是否可以通过操作开关使全部灯都打开
# ==============================================================
# run with： python Switch.py
# ==============================================================
# 思路：
# 在一维翻转问题的基础上解决二维问题
# 遍历第一层的翻转情况，在第一层确定后，在翻转第二层时，就必须考虑第一
# 层的翻转，因此情况大大减少。
# ==============================================================
# 更多细节，这篇博客讲的比较好，这里不再赘述：
# https://www.cnblogs.com/astonc/p/10849312.html
# ==============================================================

# List2D = list(list(int))
import copy

# 1<->0
flip = lambda x:1-x

# 翻转第i行第j个及其上下左右
def flip_arr(input, i, j):
    n = len(input)
    input[i][j] = flip(input[i][j])
    if(i-1>=0):
        input[i-1][j] = flip(input[i-1][j])
    if(i+1<n):
        input[i+1][j] = flip(input[i+1][j])
    if(j-1>=0):
        input[i][j-1] = flip(input[i][j-1])
    if(j+1<n):
        input[i][j+1] = flip(input[i][j+1])

# 贪心算法 
def greedy(input,res_arr):
    n = len(input)
    for i in range(n-1):
        for j in range(n):
            if(input[i][j]==1):
                flip_arr(input, i+1, j)
                res_arr[i+1][j] = 1
    if 1 in input[n-1]:
        return False
    return True

# 翻转开关
def switch(input):
    arr = copy.deepcopy(input)
    n = len(arr)
    res_arr = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(pow(2,n)): # 遍历第一行的所有可能，共有2^n种
        a = str(bin(k))[2:] # 转为二进制
        a = '0'*(n-len(a))+a # 补齐0
        for idx,c in enumerate(a):
            if c == '1':
                arr[0][idx] = flip(arr[0][idx])
                arr[1][idx] = flip(arr[1][idx])
                if((idx-1)>=0):
                    arr[0][idx-1] = flip(arr[0][idx-1])
                if((idx+1)<n):
                    arr[0][idx+1] = flip(arr[0][idx+1])
        res = greedy(arr, res_arr)
        if(res):
            print(res_arr)
            return
    print('IMPOSSIBLE!')
                    
        
t = [[1, 0, 0, 1], 
     [0, 1, 1, 0], 
     [0, 1, 1, 0],
     [1, 0, 0, 1]]

switch(t)