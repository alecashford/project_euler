function multiples_calc(max) {
	var answer = 0
	while (max > 0) {
		max -= 1
		if (max % 3 == 0 || max % 5 == 0) {
			answer += max
		}
	}
	return answer
}

console.log(multiples_calc(1000))