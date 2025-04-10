try:
	a = int(input("Berilgan a: "))

	if a > 0:
		print("Natija:", a*1)
	elif a < 0:
		print("Natija:", a*-1)
	else:
		print("Natija:", 0)

except Exception as e:
	print("Xatolik:", e)
