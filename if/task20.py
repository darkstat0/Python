try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	if a < b < c:
		print("Natija:", 1)
	elif a > b > c:
		print("Natija:", 2)
	elif a < b > c:
		print("Natija:", b)
	elif a == b == c:
		print("Natija:", 5)
	else:
		print("Natija:", 0)
except Exception as e:
	print("Xatolik:", e)
