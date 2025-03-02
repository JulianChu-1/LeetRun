from typing import Counter

def findAnagrams(s: str, p: str):
    # 能用但超时
    pp = str(sorted(p))
    n = len(p)
    res = []

    for i in range(len(s) - n):
        if str(sorted(s[i:i + n])) == pp:
            res.append(i)

    return res

def find2(s, p):
    res = []
    cnt = Counter(p)
    left = 0

    for right, c in enumerate(s):
        cnt[c] -= 1
        while cnt[c] < 0:
            cnt[s[left]] += 1
            left += 1
        if right - left + 1 == len(p):
            res.append(left)
    
    return res

print(find2("cbaebabacd", "abc"))