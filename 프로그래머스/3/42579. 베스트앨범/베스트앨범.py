from collections import defaultdict,Counter
import heapq
def solution(genres, plays):
    genreDict = defaultdict(list)
    countPlay = Counter()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genreDict[genre].append((-play,i))
        countPlay[genre]+=play
    
    answer = []
    for genre,play in countPlay.most_common():
        l = genreDict[genre]
        heapq.heapify(l)
        for i in range(2):
            if(l) :
                answer.append(heapq.heappop(l)[1])

    return answer