def solution(phone_book):
    book = set(phone_book)
    for num in phone_book:
        for i in range(1,len(num)):
            if(num[:i] in book):
                return False
    return True