class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                      90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        roman_str = []

        if num in roman_dict:
            return roman_dict[num]
        while num > 0:
            for i in range(len(nums)-1, -1, -1):
                if num in roman_dict:
                    roman_str.append(roman_dict[num])
                    num = 0
                    break
                if num > nums[i]:
                    num -= nums[i]
                    roman_str.append(roman_dict[nums[i]])
                    break

        return ''.join(roman_str)