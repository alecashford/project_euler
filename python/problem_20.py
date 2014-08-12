
def factorialize(max):
	return sum(map(int, str(reduce(lambda x, y: x*y, range(1, max + 1)))))

print factorialize(100)