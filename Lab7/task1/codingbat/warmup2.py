#1
def string_times(s, n):
    return s * n

#2
def front_times(s, n):
    return s[:3] * n

#3
def string_bits(s):
    return s[::2]

#4
def string_splosion(s):
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    return result

#5
def last2(s):
    if len(s) < 2:
        return 0

    last = s[-2:]
    count = 0

    for i in range(len(s) - 2):
        if s[i:i+2] == last:
            count += 1

    return count

#6
def array_count9(nums):
    return nums.count(9)

#7
def array_front9(nums):
    return 9 in nums[:4]

#8
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

#9
def string_match(a, b):
    count = 0
    length = min(len(a), len(b))

    for i in range(length - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1

    return count

