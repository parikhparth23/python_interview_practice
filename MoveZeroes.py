def moveZeroes(nums):
    """
        Do not return anything, modify nums in-place instead.
        """
    count = 0
    j = 0

    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
        else:
            count += 1

    for i in range(j, len(nums)):
        nums[i] = 0

    print(nums)


moveZeroes([0, 1, 0, 3, 12])
