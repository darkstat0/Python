a = int(input("Berilgan a: "))
b = int(input("Berilgan b: "))
c = int(input("Berilgan c: "))

evens = sum(x % 2 == 0 for x in (a, b, c))
print(f"Natija: {1}" if evens == 2 else f"Natija: {2}" if evens == 1 else 3)
