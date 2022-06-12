import random

nums = [0, 1, 2, 3]

for i in range(len(nums)):
    randomIndex = random.randint(0, 3)
    nums[randomIndex], nums[i] = nums[i], nums[randomIndex]

print(nums)
