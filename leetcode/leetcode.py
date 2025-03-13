from typing import List, Optional
from list_node import ListNode
import math


class Solution:
    ########################################################################
    # 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0, len(nums)):
            for inner in range(index+1, len(nums)):
                sum = nums[index] + nums[inner]
                if sum == target: 
                    return [index, inner]
                
    ########################################################################
    def merge_sorted_arrays(self, nums1 : List[int], nums2 : List[int]) -> List[int]:
        i, j = 0, 0
        merged = []
        
        # Merge while both arrays have elements
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements from nums1 or nums2
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        return merged
    
    ########################################################################    
    # 2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curl1, curl2 = l1, l2
        next1, next2 = True, True

        node_val = 0
        inner_res = res
        while True:
            if next1 is not False:
                node_val += curl1.val
            if next2 is not False:
                node_val += curl2.val

            inner_res.val = node_val % 10
            node_val //= 10
            
            next1 = False
            if curl1.next is not None:
                curl1 = curl1.next
                next1 = True
            
            next2 = False
            if curl2.next is not None:
                curl2 = curl2.next
                next2 = True
            
            if next1 is True or next2 is True:
                inner_res.next = ListNode()
                inner_res = inner_res.next
            else:
                if node_val != 0:
                    inner_res.next = ListNode()
                    inner_res = inner_res.next
                    inner_res.val = node_val
                break

        return res
    
    ########################################################################
    # 3
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_set = set()
        longest = 0
        count = 0

        i=0
        while i<len(s):
            if s[i] not in str_set:
                str_set.add(s[i])
                count+=1
                i+=1
            else:
                # look for previous char (reverse range until 0)
                for j in range(i-1, -1, -1):
                    if s[j]==s[i]:
                        i=j+1
                        break
                str_set.clear()
                count = 0
            longest = max(count, longest)

        return longest


    ########################################################################
    # 4
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        merged = []
        
        # Merge while both arrays have elements
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        length = len(merged)
        pos = int(length / 2)
        if length % 2 == 0:
            return (merged[pos]+merged[pos-1])/2.0
        else:
            return merged[pos]

    ########################################################################
    # 5 
    def longestPalindrome(self, s: str) -> str:

        def is_palindrome(i, j) -> bool:
            left = i
            right = j
            
            while left<right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if is_palindrome(start, start + length - 1):
                    return s[start : start + length]

    ########################################################################
    # 6 ZigZag
    def convertStrToVerticalCol(self, s: str, numRows: int) -> str:
        # ABC DEF AB , 3 ==> ceil 8 / 3  = 2.6 => 3
        # 036 147 25
        # 000 111 22
        #
        # A D A
        # B E B
        # C F
        #
        # PAYPALISHIRING , 3 == "PAHNAPLSIIGYIR"
        
        
        # P   A   H   N
        # A P L S I I G
        # Y   I   R
        length = len(s)
        res = list('\0' * length )
        col_size = math.ceil(length/numRows)
        for index in range(length):
            col_pos = index % col_size
            row_pos = int( index / numRows )
            pos = row_pos + col_pos * col_size
            res[pos]=s[index]
            
        return "".join(res)

    ########################################################################    
    # 6 Reverse integer
    def reverseInt(self, x: int) -> int:
        num = x
        reverse = 0
        if x > 0:
            while num > 0:
                digit = num % 10
                num //= 10
                reverse = reverse * 10 + digit
        else:
            while num < 0:
                digit = num % -10
                num = math.ceil(num/10)
                reverse = reverse * 10 + digit
                
        if reverse > 2**31 - 1 or reverse <  -2**31:
            reverse = 0
            
        return reverse
    
    ########################################################################    
    # 6 string to integer
    def myAtoi(self, s: str) -> int:
        res = 0
        parse = False

        multiplier = 1
        for chr in s:

            if parse is False:
                if chr.isspace():
                    continue
            
                if chr == '-':
                    parse = True
                    multiplier = -1
                    continue

                if chr == '+':
                    parse = True
                    continue
                
                if chr.isdigit() == False:
                    break

            if chr.isdigit() == True:
                res = res * 10 + int(chr)
                parse = True
                if multiplier == 1 and res > 2**31 - 1:
                    return 2**31 - 1
                if multiplier == -1 and res > 2**31:
                    return -2**31
                
            elif parse is True:
                break

        return res * multiplier
        
        
########################################################################
s = Solution()

########################################################################
t = s.twoSum([1,2,4], 6)
assert t == [1,2]
t = s.twoSum([2,7,11,15], 18)
assert t == [1,2]
t = s.twoSum([3,2,4], 7)
assert t == [0,2]
t = s.twoSum([3,3], 6)
assert t == [0,1]

########################################################################
first = [1, 4, 8]
second = [1, 3, 4, 17]
t = s.merge_sorted_arrays(first, second)
assert t == [1, 1, 3, 4, 4, 8, 17]

########################################################################
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
t = s.addTwoNumbers(l1, l2)
assert t.val == 7
assert t.next.val == 0
assert t.next.next.val == 8


assert s.lengthOfLongestSubstring("abcabcbb") == 3
assert s.lengthOfLongestSubstring("vvvv") == 1
assert s.lengthOfLongestSubstring("pwwkew") == 3
assert s.lengthOfLongestSubstring("aab") == 2
assert s.lengthOfLongestSubstring("dvdj") == 3


assert s.findMedianSortedArrays([1,3],[2]) == 2
assert s.findMedianSortedArrays([1,3],[2,4]) == 2.5

assert s.longestPalindrome("babad") == "bab"
assert s.longestPalindrome("cbbb") == "bbb"

def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s)-1
    while l<r:
        #print("A:", l, r)
        if s[l] != s[r]:
            #print("STOP:", l, r)
            return False
        
        l += 1
        r -= 1

    return True


assert isPalindrome("abcdef") == False
assert isPalindrome("abcde") == False
assert isPalindrome("aba") == True
assert isPalindrome("abba") == True
assert isPalindrome("abcba") == True

# Error
#assert s.convertStrToVerticalCol("ABCDEFABC", 3) == "ADABEBCFC"
#assert s.convertStrToVerticalCol("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"

assert s.reverseInt(123) == 321
assert s.reverseInt(-120) == -21
assert s.reverseInt(1534236469) == 0 # bigger than max int 9646324351
assert s.reverseInt(-1534236469) == 0 # smaller than max int 9646324351
assert s.reverseInt(12345) == 54321
assert s.reverseInt(-12345) == -54321


assert s.myAtoi("      00042") == 42
assert s.myAtoi("     -00042") == -42
assert s.myAtoi("  42c42    ") == 42
assert s.myAtoi(" 9646324351") == 2**31-1 # bigger than max int 9646324351
assert s.myAtoi("-9646324351") == -2**31 # smaller than max int 9646324351
assert s.myAtoi("WORD 964351") == 0 # smaller than max int 9646324351
