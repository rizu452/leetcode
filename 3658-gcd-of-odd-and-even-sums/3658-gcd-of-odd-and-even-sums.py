class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # temp=n
        sumOdd=0
        sumEven=0
        i=n*2
        while i>0:
            if i%2==0:
                sumEven+=i
            else:
                sumOdd+=i
            i-=1
        # if sumOdd>sumEven:
        #     smallest=sumEven
        # else:
        #     smallest=sumOdd

        # j=smallest
        # while j>=1:
        #     if sumOdd%j==0 and sumEven%j==0:
        #         return j
        #     j-=1
        a=sumOdd
        b=sumEven
        while b!=0:
            remainder=a%b
            a=b
            b=remainder
        return a