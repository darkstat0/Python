try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	print("true" if a + b > c and b + c > a and c + a > b else "Natija: false")
except Exception as e:
	print("Xatolik:", e)
