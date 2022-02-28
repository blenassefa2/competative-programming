def get_winner(peoples):
    winner = 0
    tie = False
    for x in range(len(peoples)):
        if peoples[x] > peoples[winner]:
            winner = x
            tie = False
        elif x != winner and peoples[x] == peoples[winner]:
            tie = True
    
    
    return (tie,winner)
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons =  persons
        self.times = times
        peoples = [0]*(max(persons)+1)
        self.winners= []
        for i in range(len(times)):
            
            peoples[self.persons[i]] += 1
            
            winner = get_winner(peoples)
            
            if not winner[0]:
                self.winners.append(winner[1])
            else:
                x = i
                while x >=0 :
                    if peoples[self.persons[x]] == peoples[winner[1]]:
                        break
                    x-= 1
                self.winners.append(self.persons[x])
                    
            
            
        
        
    def q(self, t: int) -> int:
       
        best =  -1
        left = 0
        right = len(self.times) - 1
        while right >= left:
            mid = int(left + (right - left)/2)
            
            if self.times[mid] > t:
                right  = mid - 1
            else:
                best = mid
                left = mid + 1
        return self.winners[best]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)