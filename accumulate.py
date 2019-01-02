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

	def add2(a, b): return a + b

	def suml(seq): return foldl(add2, 0, seq)

	assert(suml(list(range(10))) == 45)

	def sumr(seq): return foldr(add2, 0, seq)

	assert(sumr(list(range(10))) == 45)
