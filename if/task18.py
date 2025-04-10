try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))

	if a < b:
		print(a)
	elif b < a:
		print(b)
	else:
		print("teng")
except Exception as e:
	print("Xatolik:", e)
