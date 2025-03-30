try:
	a = int(input("Input: "))

	if a%3 == 0 or a%4 == 0:
		print("Output: true")
	else:
		print("Output: false")
except (ValueError, EOFError):
	print("Dasturga son kiriting!")
