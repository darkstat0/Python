try:
	a = int(input("Input: "))

	if a > 0:
		print('musbat')
	elif a < 0:
		print('manfiy')
	else:
		print(a)
except ValueError:
	print('Dasturga son kiriting!')
