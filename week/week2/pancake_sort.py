import random
class Solution:
    def is_sorted(self, arr):
        for t in range(len(arr)-1):
            if arr[t] > arr[t +1]:
                return False
        return True
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []

        l = len(arr)
        i = 0
        while not self.is_sorted(arr):

            t, c = arr[:l-i], arr[l-i:]
            k = t.index(max(t)) +1
            a, b = t[:k], t[k:]
            if k != 1:
                ans.append(k)
                a.reverse()

            a.extend(b)
            ans.append(len(t))
            a.reverse()
            arr = a
            arr.extend(c)
            i+=1
        return ans