function even_fibonacci(max) {
	var term_1 = 0
	var term_2 = 1
	var new_term = 0
	var even_fibs = []
	while (new_term < max) {
		new_term = term_1 + term_2
		if (new_term % 2 == 0) {
			even_fibs.push(new_term)
		}
		term_1 = term_2
		term_2 = new_term
	}
	return even_fibs.reduce(function(a, b) {
		return a + b
	})
}

console.log(even_fibonacci(4000000))

// answer = 4613732