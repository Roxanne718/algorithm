# =============================================================
# 最长上升子序列（LIS）：输入一组数，输出其中的最长上升子序列长度
# =============================================================
# 思路：需要维护两个值：当前LIS的最后一个元素，以及对应的长度
# =============================================================

# ====================================================
# solution1：dp[最后一个元素]=长度，时间复杂度O(n^2)
# ====================================================
def solution1(string=[2,5,3,4,1,7,6]):
    dp = [1 for _ in range(len(string))]
    for i in range(len(string)):
        for j in range(i):
            if(string[j]<string[i] and (dp[j]+1)>dp[i]):
                dp[i] = dp[j]+1
    print(max(dp))
    
# ====================================================
# solution2：dp[长度]=最后一个元素，时间复杂度O(nlogn)
# ====================================================
def binary_search(mylist, num, l=0, r=None): # 二分查找
    if(r==None):
        r = len(mylist)
    if((r-l)==1):
        return l
    mid = l + ((r-l)//2)
    if(mylist[mid]>num):
        return binary_search(mylist, num, l, mid)
    elif(mylist[mid]<num):
        return binary_search(mylist, num, mid, r)

def solution2(string=[2,5,3,4,1,7,6]):
    dp = [None, string[0]]
    for i in range(1, len(string)):
        index = binary_search(dp, string[i])+1 # 以string[i]结尾的LIS长度,dp[index]=LIS
        if(len(dp)<=index):
            dp.append(string[i])
        else:
            dp[index]=min(string[i],dp[index])
    print(len(dp)-1)

test0 = [5,4,1,2,3] # 3
test1 = [4,2,4,5,3,7] # 4
solution1(test0)
solution2(test0)
    