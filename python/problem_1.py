def multiples_calc(max):
	answer = 0
	while max > 0:
		max -= 1
		if max % 3 == 0 or max % 5 == 0:
			answer += max
	return answer

print multiples_calc(1000)