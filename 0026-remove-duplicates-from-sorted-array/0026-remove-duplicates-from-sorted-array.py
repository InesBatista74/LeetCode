class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0                          # posição do último valor único
        for j in range(1, len(nums)):  # escolha de um dos elementos de nums
            if nums[j] != nums[i]:     # encontramos um valor diferente do último valor único
                i += 1
                nums[i] = nums[j]

        return i + 1                   # número de elementos únicos
