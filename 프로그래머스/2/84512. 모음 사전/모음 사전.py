def solution(word):
    alphaSet = 'AEIOU'
    count = [-1]
    def dfs(current):
        
        if len(current) > 5: 
            return False
        
        count[0] += 1
        
        if current == word:
            return True
        
        for s in alphaSet:
            if dfs(current + s):
                return True
        return False

    dfs('')
    return count[0]