a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
c = int(input("Berilgan c: "))

zero = sum(x == 0 for x in (a, b, c))
print(f"Natija: 0" if zero == 1 else "Natija:", (a*100+b*10+c))
