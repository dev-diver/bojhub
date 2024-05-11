def generate_combinations():
    sequence = ['A']
    
    while True:
        yield ''.join(sequence) 
        
        if len(sequence) < 5:
            sequence.append('A') 
        else:
            for i in range(4, -1, -1):
                if sequence[i] != 'U':
                    next_char_index = 'AEIOU'.index(sequence[i]) + 1
                    sequence[i] = 'AEIOU'[next_char_index]
                    sequence = sequence[:i+1] 
                    break
                if i == 0:
                    return
                sequence[i] = 'A'

def solution(word):
    cnt = 1
    for combo in generate_combinations():
        if combo == word:
            return cnt
        cnt += 1