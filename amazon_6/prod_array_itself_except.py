# Logic: just take one and go on both directions
# Time: O(N)
# Space: O(1)

def productExceptSelf(self, nums):
    if nums:
        len_nums = len(nums)
        output = []

        p = 1
        for i in range(len_nums):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(len_nums - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output