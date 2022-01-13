# ===============================
# 矩阵快速幂计算斐波那契数列
# F(0) = 0
# F(1) = 1
# F(N) = F(N-1)+F(N-2)
# ===============================
# run with： python Fibonacci.py
# ===============================

# 矩阵乘法（2*2）
def matricx_pow(A, B):
    return [[ A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [ A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

# 快速幂
def quick_power(A, n):
    if(n==1):
        return A
    if(n==2):
        return matricx_pow(A, A)
    if(n%2==0):
        tmp = quick_power(A, n/2)
        return matricx_pow(tmp,tmp)
    else:
        tmp = quick_power(A, (n-1)/2)
        return matricx_pow(matricx_pow(tmp,tmp), A)

def fibonacci(n):
    if(n==1 or n==2):
        return 1
    A = [[1,1],[1,0]]
    b = [[1],[1]]
    A_n = quick_power(A, n-2)
    res = A_n[0][0]+A_n[0][1]
    return res

for i in range(1,101):
    print(i, fibonacci(i), flush=True)