try:
	a = int(input("Berilgan son: "))

	if a%4 == 0 or a%(100 or 400) == 0:
		print("Natija: true")
	else:
		print("Natija: false")
except (ValueError, EOFError):
	print("Dasturga son kiriting!")
