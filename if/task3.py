try:
	a = int(input("Input: "))
	print("Output:", a%3)
except (ValueError, EOFError):
	print("Dasturga son kiriting!")
