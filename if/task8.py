try:
	a = int(input("Input: "))

	if a%5 == 0:
		print("true")
	else:
		print("Output: false")
except (ValueError, EOFError):
	print("Dasturga son kiriting!")
