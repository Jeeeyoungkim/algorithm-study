N, S = map(int, input().split())
num_list = list(map(int, input().split()))

sum_cnt = 0

def dfs(idx, current_sum):
    global sum_cnt
    
    if idx == N:
        return
    
    if current_sum + num_list[idx] == S:
        sum_cnt += 1
    
    dfs(idx+1, current_sum + num_list[idx])
    dfs(idx+1, current_sum)
    
dfs(0, 0)
print(sum_cnt)
    