try:
	a = int(input("Berilgan a: "))
	b = int(input("Berilgan b: "))
	c = int(input("Berilgan c: "))

	if a == b and b == c:
		print("equilateral")
	elif a == c:
		print("isosceles")
	else:
		print("scalene")
except Exception as e:
	print("Error:", e)
