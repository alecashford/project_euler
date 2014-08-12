
def factorialize(max)
	range_product = (1..max).to_a.reduce(:*).to_s
	puts range_product.split("").map{|num| num.to_i}.reduce(:+)
end

factorialize(100)