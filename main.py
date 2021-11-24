def medians(nums1,nums2):
    nums = nums1 + nums2
    nums.sort()
    
    if len(nums)%2 == 0:
        return (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
    else:
        return nums[len(nums)//2]
