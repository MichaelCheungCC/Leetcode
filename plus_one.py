# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_reverse=digits[::-1]
        special_case=1
        for i in range(len(digits)):
            if digits_reverse[i]<9:
                digits_reverse[i]=digits_reverse[i]+1
                special_case=0
                break
            else:
                digits_reverse[i]=0
        if special_case==1:
            return [1] + digits_reverse[::-1]
        return digits_reverse[::-1]