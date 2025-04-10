try:
	def count_positive_numbers(a, b, c):
		count = 0
		if a > 0:
			count += 1
		if b > 0:
			count += 1
		if c > 0:
			count += 1
		return count

		a = int(input("Berilgan a: "))
		b = int(input("Berilgan b: "))
		c = int(input("Berilgan c: "))

		result = count_positive_numbers(a, b, c)
		print(f"Natija: {result}")
except Exception as e:
	print("Xatolik:", e)
