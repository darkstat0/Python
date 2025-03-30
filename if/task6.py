try:
	a = int(input("Input a: "))
	b = int(input("Input b: "))
	c = int(input("Input c: "))

	if a > b and a > c:
		print(f"katta son a={a}")
	elif b > a and b > c:
		print(f"katta son b={b}")
	elif c > a and c > b:
		print(f"katta son c={c}")
except (ValueError, EOFError):
	print("Dasturga son kiriting!")
