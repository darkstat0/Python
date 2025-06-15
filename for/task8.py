a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
son = []

for i in range(a, b):
	if i%3 == 0:
		son.append(i)

print("yig'indi =", sum(son))
print("soni =", len(son))
