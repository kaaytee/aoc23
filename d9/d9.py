def extrapolat(nums):
    if all(x == 0 for x in nums):
        return 0
    d = [y - x for x, y in zip(nums, nums[1:])]
    diff = extrapolat(d)
    return nums[-1] + diff

def extrapolate_front(nums):
    if all(x == 0 for x in nums):
        return 0
    d = [y - x for x, y in zip(nums, nums[1:])]
    diff = extrapolate_front(d)
    return nums[0] - diff

# def sol(file):
#     total = 0
#     with open(file, 'r') as f:
#         for line in f:
#             nums = list(map(int, line.split()))
#             total += extrapolat(nums)
    
#     return total
    
    
def sol(file):
    total = 0
    with open(file, 'r') as f:
        for line in f:
            nums = list(map(int, line.split()))
            total += extrapolate_front(nums)
    
    return total
    
print(sol('input.txt'))
    