nums = range(1,101L)
squares = map(lambda x: x*x, nums)
x = sum(nums)
print x*x-sum(squares)
