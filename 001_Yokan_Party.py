N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

def solve(least:int) -> bool:
    pre = 0
    count = 0
    for i in range(N):
        if A[i] - pre >= least and L - A[i] >= least:
            count += 1
            pre = A[i]
    return True if count >= K else False

left = 0
right = L
max_lseast = 0
while(left<=right):
    mid_len = (left + right) // 2
    if solve(mid_len):
        left = mid_len + 1
        max_lseast = max(max_lseast,mid_len)
    else: right = mid_len - 1

print(max_lseast)