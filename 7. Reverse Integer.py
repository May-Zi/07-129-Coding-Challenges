class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            y= str(x)
            x=(-1)*int(y[:0:-1])
            if x>=(-2**31) and x<=(2**31-1):
                return x
        elif x>0:
            y= str(x)
            x=int(y[::-1])
            if x>=(-2**31) and x<=(2**31-1):
                return x
        elif x==0:
            return x
        return 0
