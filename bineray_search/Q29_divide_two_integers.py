class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            if abs(dividend) < abs(divisor):
                return 0  # -2 / 10 = 0
        sum = 0
        counter = 0
        res = 0
        
        a = abs(dividend)
        b = abs(divisor)
        
        while a >= b:
            sum = b
            counter = 1
            while sum + sum <= a:
                sum += sum
                counter += counter
            a -= sum
            res += counter
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res        
        