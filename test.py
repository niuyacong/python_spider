
class Analyser():
    def analysis(self,htmls):
        pass

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    result.append(nums[i])
                    result.append(nums[j])
                    return result
                
                
a=Solution()
print(a.twoSum([2, 7, 11, 15],26))