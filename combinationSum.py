class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []

        def dfs(index, temp):
            if temp == 0:
                result.append(path[:])
                return
            if temp < 0 or index >= len(nums) :
                return
            # calculate and add all subset which don't include nums[index]
    
            dfs(index+1, temp)
            # calculate and add all subsets which DO include nums[index]
            path.append(nums[index])
            remaining = temp - nums[index]
            dfs(index, remaining)
            path.pop()
            
        
        dfs(0,target)
        return result
