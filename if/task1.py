try:
    a = int(input("Input: "))

    if 10 < a:
        print("Output:", a + 3)
    elif 10 > a:
        print("Output:", a * 2)
    elif 10 == a:
        print("Output:", 22)
except ValueError:
    print("Dasturga son kriting!")
