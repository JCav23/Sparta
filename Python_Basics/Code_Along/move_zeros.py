# LeetCode75 : 283 - Move Zeros
# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

def move_zeroes(nums):
    for num in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)
    return nums


numbers = [2, 1]
print(move_zeroes(numbers))
