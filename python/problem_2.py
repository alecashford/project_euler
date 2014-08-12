def even_fibonacci(max):
	term_1 = 0
	term_2 = 1
	new_term = 0
	even_fibs = []
	while new_term < max:
		new_term = term_1 + term_2
		if new_term % 2 == 0:
			even_fibs.append(new_term)
		term_1 = term_2
		term_2 = new_term
	return sum(even_fibs)

print even_fibonacci(4000000)

# answer = 4613732