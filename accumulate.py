def accumulate(op, init, seq):
	if seq:
		return op(seq[0], accumulate(op, init, seq[1:]))
	else:
		return init

foldr = accumulate

def foldl(op, init, seq):
	for item in seq:
		init = op(init, item)
	return init

if __name__ == "__main__":

	# foldr and foldl should be equivalent to each other if:
	# op is commutative
	def add2(a, b): return a + b
	def sum_l(seq): return foldl(add2, 0, seq)
	def sum_r(seq): return foldr(add2, 0, seq)
	assert(sum_l(list(range(10))) == sum_r(list(range(10))))