def solution(sides):
    max_side = max(sides)
    
    # 배열에 가장 긴 변이 있는 경우
    answer_side_1 = [val for val in range(max_side+1) if max_side < val + min(sides)]
    # 나머지 한 변이 가장 긴 변인 경우
    answer_side_2 = [val for val in range(max_side+1, sum(sides)) if val < sum(sides)]

  
    return len(answer_side_1) + len(answer_side_2)