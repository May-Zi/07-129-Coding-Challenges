class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        List = ['I', 1,'V', 5,'X', 10,'L', 50,'C', 100,'D', 500,'M', 1000]
        total = 0
        prev = 0
        for i in s:
            current = List[List.index(i)+1]
            if(prev < current):
                total += current - prev
                total -= prev
            else:
                total += current
            prev = current
        return total
