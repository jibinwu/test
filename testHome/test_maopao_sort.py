import random
import pytest

def maopao_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                print(nums)
    # return random.choice([nums,None,10])
    return nums
print(maopao_sort([13,1,2,5,3]))
