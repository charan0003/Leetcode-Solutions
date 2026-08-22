class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        digit_sum=0
        digit_prod=1

       
        while n>0:
            digit=n%10
            digit_sum+=digit
            digit_prod*=digit
            n//=10
        total=(digit_sum)+(digit_prod)
        return original%total==0