#1
def count_evens(nums):
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1
    return count

#2
def big_diff(nums):
    return max(nums) - min(nums)

#3
def centered_average(nums):
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1]
    return sum(trimmed) // len(trimmed)

#4
def sum13(nums):
    total = 0
    skip = False

    for n in nums:
        if n == 13:
            skip = True
            continue
        if skip:
            skip = False
            continue
        total += n

    return total

#5
def sum67(nums):
    total = 0
    skip = False

    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n

    return total

#6
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

