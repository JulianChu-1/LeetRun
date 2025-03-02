class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        window = {}

        while right < len(s):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            
            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res