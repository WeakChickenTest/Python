def test_a():
    name = "文晋国"
    print(name)
def test_b():
    tag = 1
    print(tag)
    try:
        a = 10
        b = 0
        c =a/b
        print(c)
    except ZeroDivisionError:
        print("被除数不能为0")
