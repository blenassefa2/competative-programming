class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums2)
        stack = []
        i = 0
        while i < (len(nums2)):
            if not (bool(stack)):
                stack.append(i)
                i+=1
                continue
            last = stack[-1]

            if nums2[last] <nums2[i]:

                ans[last] =nums2[i]
                stack.pop()
                if not (bool(stack)) or nums2[stack[-1]] > nums2[i]:
                    stack.append(i)
                    i+=1
                    continue
            else:
                stack.append(i)
                i+=1
        final = []
        for i in nums1:
            final.append(ans[nums2.index(i)])
        return final
        
                