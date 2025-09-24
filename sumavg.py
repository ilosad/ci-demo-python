def _v(nums):
    if nums is None: raise ValueError("리스트가 필요합니다.")
    nums = list(nums)
    if not nums: raise ValueError("빈 리스트입니다.")
    if not all(isinstance(x, int) for x in nums): raise ValueError("정수만 허용됩니다.")
    return nums

def sum_list(nums):
    return sum(_v(nums))

def avg_list(nums):
    n = _v(nums); return sum(n) / len(n)
