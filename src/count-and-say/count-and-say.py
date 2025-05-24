class Solution:
    def rle(self, val: str) -> str:
        res = []
        count = 1
        for i in range(1, len(val)):
            if val[i] == val[i-1]:
                count+=1
            else:
                res += [str(count), val[i - 1]]
                count=1
        # append last element - also handles 1 case
        res += [str(count), val[-1]]
        return ''.join(res)

    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        return self.rle(self.countAndSay(n-1))