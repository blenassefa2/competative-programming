class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        l = 0
        st = Deque()
        while right < len(s):
           
            while right < len(s) and s[right] not in st:
                st.append(s[right])
                right += 1
                
            l = max(l , right - left)
            left += 1
            st.popleft()
        return l
            