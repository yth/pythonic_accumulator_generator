from accumulate import accumulate

class accumulator(object):
	def __init__(self, bi_op, init, save_state=False):
		self.bi_op = bi_op
		self.init = init
		self.save_state = save_state

	def __call__(self, seq, init=None, func=None):
		if init: self.init = init

		def bi_op(a, b):
			if func:
				return self.bi_op(a, b, f=func)
			else:
				return self.bi_op(a, b)

		if self.save_state:
			self.init = accumulate(bi_op, self.init, seq)
			return self.init
		else:
			return accumulate(bi_op, self.init, seq)

if __name__ == "__main__":

	# accumulator generator a la Paul Graham
	print("Accumulator Generator Solution Demo")

	def add2(a, b): return a + b

	def foo(n):
		return accumulator(add2, n, save_state=True)

	f = foo(10)
	print(f([1]))
	print(f([1]))

"""
	# We incurred some inconvenience, but we gained more power as well
	print()
	print("We have become more powerful")
	print(f([1, 2, 3]))
	print()

	# map
	def apply_and_extend(a, b, f):
		return [f(a)] + b

	def inc1(x): return x + 1

	map = accumulator(apply_and_extend, [])
	print("map demo")
	print(map(list(range(10)), func=inc1))
	print()

	# filter
	def selective_extend(a, b, f):
		if f(a):
			return [a] + b
		else:
			return b

	def gt_2(x):
		return x > 2

	filter = accumulator(selective_extend, [])
	print("filter demo")
	print(filter(list(range(10)), func=gt_2))
	print()

	# chaining functions
	print("chaining filter and map")
	print(map(filter(list(range(10)), func=gt_2), func=inc1))
	print()

	import sys

	print("Current Recursion Limit: {}".format(sys.getrecursionlimit()))
"""