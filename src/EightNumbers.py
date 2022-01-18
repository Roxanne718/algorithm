# ===================================
# 九个格子中放入了数字 1 ∼ 8方块，
# 利用空位移动方块，问使数字恢复顺序
# 所需最少移动次数？
# ===================================
# 思路：
# 求最少移动次数，应该使用广度优先搜索
# 康托展开 + 双向广度优先搜索
# 康托展开 : X = an(n − 1)! + an−1(n − 2)! + · · · + a1 × 0!
# ===================================
import copy
import math

factorial = [math.factorial(i) for i in range(9)] # 0!,1!,2!,3!,4!,5!,6!,7!,8!

bfs = [] # (hash, attr, depth)


origin = [[3,1,2],
          [0,4,5],
          [6,7,8]]

target = [[3,0,1],
          [4,5,2],
          [6,7,8]]

def cantor(arr):
    tmp = []
    c = 0
    # 2D -> 1D
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            tmp.append(arr[i][j]) 
    # X = an(n − 1)! + an−1(n − 2)! + · · · + a1 × 0!
    for i in range(len(tmp)):
        idx = 0
        for j in range(i+1,len(tmp)): # 找出比tmp[i]小的数有多少
            if(tmp[i]>tmp[j]):
                idx+=1
        c += factorial[len(tmp)-1-i]*idx
    return int(c)

# 559 -> 542136
def incantor(hash, n=9):
    tmp = [i for i in range(0,n)] # 第0到第n-1大的数
    res = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(n-1,-1,-1):
        c = hash//factorial[i]
        hash = hash%factorial[i]
        # print(f'i={i}  c={c}  hash={hash}   tmp={tmp}')
        # print(f'{i//3} {i%3} {c}')
        res[2-(i//3)][2-(i%3)] = tmp[int(c)]
        tmp.pop(c)
    return res

def find0(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j]==0):
                return i,j
            
_flip = lambda x:'e' if x=='s' else 's'

def finditem(mylist:list, myitem:tuple)->tuple:
    hash, attr, depth = myitem # cantor, 's' or 'e', depth
    for h, a, d in mylist:
        if(h==hash and a==_flip(attr)):
            return (True,d+depth)
    return False,0

def bibfs():
    while (len(bfs)>0):
        item = bfs.pop(0) # (_hash, _attr, _depth)
        item_arr = incantor(item[0])
        i, j = find0(item_arr)
        
        found,d = finditem(bfs, item)
        if found:
            print(d)
            break
        
        if(i>0): # up
            arr_up = copy.deepcopy(item_arr)
            arr_up[i][j],arr_up[i-1][j]=arr_up[i-1][j],arr_up[i][j] # swap
            newitem = (cantor(arr_up),item[1],item[2]+1)
            bfs.append(newitem)

        if(i<2): # down
            arr_down = copy.deepcopy(item_arr)
            arr_down[i][j],arr_down[i+1][j]=arr_down[i+1][j],arr_down[i][j] # swap
            newitem = (cantor(arr_down),item[1],item[2]+1)
            bfs.append(newitem)
        
        if(j>0): # left
            arr_left = copy.deepcopy(item_arr)
            arr_left[i][j],arr_left[i][j-1]=arr_left[i][j-1],arr_left[i][j] # swap
            newitem = (cantor(arr_left),item[1],item[2]+1)
            bfs.append(newitem)

        if(j<2): # right
            arr_right = copy.deepcopy(item_arr)
            arr_right[i][j],arr_right[i][j+1]=arr_right[i][j+1],arr_right[i][j] # swap
            newitem = (cantor(arr_right),item[1],item[2]+1)
            bfs.append(newitem)

bfs.append((cantor(origin),'s',0))
bfs.append((cantor(target),'e',0))
bibfs()

# test = [[1,2,3],
#         [4,5,6],
#         [7,8,0]]
# t = cantor(test)
# print(t)
# print(incantor(t))