def threeSum(nums):
    size=len(nums)
    nums.sort()
    print(nums)
    pass
    ans=[]
    for i in range(0, size-2):
            r=size-1
            l=i+1
            while l < r:
                if nums[i]+nums[l]+nums[r] == 0:
                    ans.insert(0,[nums[i],nums[l],nums[r]])
                    break
                if nums[i]+nums[l]+nums[r] < 0:
                    l+=1
                if nums[i]+nums[l]+nums[r]  > 0:
                    r-=1
                print("while",l,r)
    return ans
    # return False
threeSum([-1, 0, 1, 2, -1, -4])