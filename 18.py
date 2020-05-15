from collections import defaultdict
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Store a dp style table of [row][col] for each two sum
        dp = {}
        res = set()
        seen = defaultdict(list)
        # 1
        for r in range(len(nums)):
            for c in range(r):
                have = nums[r] + nums[c]
                need = target - have
                # 2
                if need in seen:
                    # 3
                    for r1,c1 in seen[need]:
                        if len({r1,c1,r,c}) == 4:
                            res.add( tuple(sorted([nums[r1],nums[c1],nums[r],nums[c]])) ) 
                seen[have].append((r, c))
        return res