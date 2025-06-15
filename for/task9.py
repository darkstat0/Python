a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))

son = []

for i in range(a, b):
	if i%2 and i%3 == 0:
		son.append(i)

print("Natija:", len(son))
