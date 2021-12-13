class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        dist = [0]*len(points)
        l = len(dist)
        temp = []
        for i in range(l):
            dist[i] = sqrt(((points[i][0])**2) + ((points[i][1])**2))
            temp.append((points[i],dist[i]))
        v = sorted(temp, key=lambda tup: (tup[1]))
        result = [v[a][0] for a in range(k)]
        return result
            