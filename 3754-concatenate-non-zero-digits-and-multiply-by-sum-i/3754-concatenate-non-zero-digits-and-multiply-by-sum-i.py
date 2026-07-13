class Solution(object):
    def sumAndMultiply(self, n):
        p = 1
        x = 0
        s = 0

        while n > 0:
            digit = n % 10

            if digit != 0:
                x += digit * p
                p *= 10

            s += digit
            n //= 10

        return x * s   