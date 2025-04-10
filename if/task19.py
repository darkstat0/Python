try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	average = (a + b + c) // 3
	print("Natija:", average)
except Exception as e:
	print("Xatolik:", e)
