n = int(input("Berilgan n: "))
son = 1
a = 0

for i in range(son, n+1):
	son = i*i
	a += son

print("Natija:", a)
