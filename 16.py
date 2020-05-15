import sys
def threeSum(nums,target):
    size=len(nums)
    nums.sort()
    print(nums)
    clossum=sys.maxsize; 
    for i in range(0, size-2):
            r=size-1
            l=i+1
            while l < r:
                sum=nums[i]+nums[l]+nums[r]
                if abs(target-sum)< abs(target-clossum):
                    clossum=sum
                if sum > target :
                    r -=1
                else :
                    l+=1
                
                    
                print("while",l,r)
    return clossum
    # return False
print(threeSum([-1, 2, 1, -4],1))
