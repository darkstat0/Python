
try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	if a == b:
		print("Natija:", c)
	elif a == c:
		print("Natija:", b)
	elif b == c:
		print("Natija:", a)
	else:
		print("Natija:", 0)
except Exception as e:
	print("Xatolik:", e)
