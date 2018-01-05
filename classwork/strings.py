def main():

	str1 = ''

	for n in range(1, 101):
		if (n < 100):
			str1 += str(n) + ', '
		else:
			str1 += str(n)

	print(str1)

	bing = 'Binghamton'
	print(bing[:3])
	print(bing[4:6] + bing[-3])
	print(bing[0] + bing[-2] + bing[5] + bing[-3])

	results = 'average: 0.8475'
	colonIndex = results.find(':')
	val = float(results[colonIndex + 2:])

	print(val)

main()
