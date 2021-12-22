class Solution:
    
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = len(nums)
        nums.sort()
        n = set(nums)
        
        Dict = defaultdict(deque)
        for i in range(len(nums)):
            Dict[nums[i]].append(i)
        print(Dict)
        value = 0
        visited =set()
        for i in range(len(nums)):
            t = nums[i]
            print(visited)
            if i not in visited and k -t not in visited:
                if k - t not in Dict.keys():
                    continue
                if len(Dict[k -t])!= 0:
                    visited.add(Dict[k -t][0])
                    Dict[k -t].popleft()
                    value+=1
                    
        print(value)

        return (value)


class Solution:
    def is_arithmetic(self,value):
        t = value[0] - value[1]
        for i in range(len(value)-1):
            if value[i] - value[i + 1] != t:
                return False

        return True
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        li =[]
        value = []
        ans = []
        for i in range(len(l)):
            li.extend(l[i] + x for x in range(len(l)))
            if r[i] not in li:
                li.append(r[i])
            for t in range(len(li)):
                if len(nums)>li[t]:
                    li[t] = nums[li[t]]
            li.sort(reverse = True)
            if self.is_arithmetic(li):
                ans.append(True)
            else:
                ans.append(False)

            li = []
            value = []
        return ans 