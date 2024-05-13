def solution(phone_book):
    book = set(phone_book)
    answer = True
    for num in phone_book:
        if(not answer): break
        for i in range(1,len(num)):
            check = num[:i]
            if(check in book):
                answer = False
                break
    return answer