class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, value in enumerate(nums):
            if i>0 and value == nums[i-1]:
                continue #skip duplicate is
            l, r = i+1, len(nums)-1 # 0 indexed
            while l<r:
                threesum = value + nums[l] + nums[r]
                if threesum == 0:
                    result.append([value, nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]: # check duplicate l pointers only 
                        l+=1
                elif threesum < 0:
                    l+=1
                else:
                    r-=1
        return result 