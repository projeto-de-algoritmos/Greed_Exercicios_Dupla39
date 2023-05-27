class Solution(object):
    def canJump(self, nums):
        atual = 0

        for i in range(len(nums) - 1):
            if i > atual:
                return False
            if i + nums[i] > atual: 
                atual = i + nums[i] 
                print(atual)
        return atual >= len(nums) - 1