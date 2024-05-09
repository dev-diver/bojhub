from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def solution(numbers):
    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(sorted_numbers)
    # 모든 숫자가 0인 경우 예외 처리
    return answer if answer[0] != '0' else '0'