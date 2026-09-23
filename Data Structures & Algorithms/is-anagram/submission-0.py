class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bucket1 = {};
        bucket2 = {};
        for char in s:
            if char in bucket1:
                bucket1[char] += 1;
            else:
                bucket1[char] = 1;
        for char in t:
            if char in bucket2:
                bucket2[char] += 1;
            else:
                bucket2[char] = 1;
        if bucket1 == bucket2:
            return True;
        else:
            return False;