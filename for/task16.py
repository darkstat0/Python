n = int(input("Berilgan n: "))
l = str(n)
l = list(l)
a = 0

for i in range(len(l)):
	son = int(l[i])
	a += son**len(l)

if n == a:
	print("Natija:", True)
else:
	print("Natija:", False)
