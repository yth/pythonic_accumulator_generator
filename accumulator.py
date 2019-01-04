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
	def add2(a, b): return a + b

	foo = accumulator
	f = foo(add2, 10, save_state=True)
	print("Accumulator Generator Solution Demo")
	print(f([1]))
	print(f([1]))
	print()

	# This is equivalent to the above
	# 	if you don't want to see the intervening step
	f = foo(add2, 10, save_state=True)
	print("Do both adds at once")
	print(f([1, 1]))
	print()

	# map
	def apply_and_append(a, b, f):
		return [f(a)] + b

	def add1(x): return x + 1

	map = accumulator(apply_and_append, [])
	print("map demo")
	print(map(list(range(10)), func=add1))
	print()

	# filter
	def selective_append(a, b, f):
		if f(a):
			return [a] + b
		else:
			return b

	def gt_2(x):
		return x > 2

	filter = accumulator(selective_append, [])
	print("filter demo")
	print(filter(list(range(10)), func=gt_2))
	print()

	import sys

	print("Current Recursion Limit: {}".format(sys.getrecursionlimit()))