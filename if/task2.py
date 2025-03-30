try:
    a = int(input("Input: "))
    b = a // 3
    print("Output:", b)
except (ValueError, EOFError):
    print("Dasturga son kiriting!")
