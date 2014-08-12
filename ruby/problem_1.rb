def multiples_calc(max)
	answer = 0
	while max > 0
		max -= 1
		if max % 3 == 0 || max % 5 == 0
			answer += max
		end
	end
	answer
end

puts multiples_calc(1000)

# answer = 233168