def maxArea(height):
        l=0
        areas=[]
        r=len(height)-1
        max=0
        while l <= r:
            print(height[l],height[r],r-l)
            area=(r-l)*min(height[l],height[r])
            if area > max :
                max=area
            areas.append(area)
            if height[l]>height[r]:
                r=r-1
            elif height[l]>height[r]:
                l=l+1
            else:
                l=l+1
        print(areas)
        print("max= ",max)
        return max
# driver
arrr=[1,8,6,2,5,4,8,3,7]
maxArea(arrr)