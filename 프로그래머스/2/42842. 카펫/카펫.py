def solution(brown, yellow):
    for height in range(1, int(yellow ** 0.5) + 1):
        if yellow % height == 0:
            width = yellow // height
            # 테두리의 갈색 격자 수 확인
            if 2 * (width + height) + 4 == brown:
                return [width + 2, height + 2]
    return []