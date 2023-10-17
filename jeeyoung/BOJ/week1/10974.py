# 10974

N = int(input())
answer_list = []
visited = [0 for _ in range(N)]

def dfs(idx, list):
    # 탈출조건
    if idx == N:
        answer_list.append(list[:])
        print(' '.join(map(str, list)))
        return
    
    for i, val in enumerate(range(1, N+1)):
        if visited[i] == 1:
            continue
        
        list.append(val)
        visited[i] = 1
        
        dfs(idx+1, list)
        
        list.pop()
        visited[i] = 0
        
dfs(0, [])
        