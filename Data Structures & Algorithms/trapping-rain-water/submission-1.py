class Solution:
    def trap(self, height: List[int]) -> int:
        l_w = r_w = 0
        s = 0
        n = len(height)
        l = [0]*n
        r = [0]*n

        for i in range(n):
            j = -i-1
            l[i] = l_w
            r[j] = r_w
            l_w = max(l_w,height[i])
            r_w = max(r_w,height[j])
        
        for i in range(n):
            p = min(l[i],r[i])
            s += max(0,p-height[i])
        return s