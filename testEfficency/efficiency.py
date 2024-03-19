from timeit import default_timer as timer
import re


stringValue = "This is a hugeeee string like seriously its big!"
scut = "  Hello, world!   \t\n"
class MyTestClass:
    x = 5


obj = MyTestClass()
my_ListObject = [1, 2, 3]

def efficiency_loop1():
    s = timer()
    for i in range(1,400000):
        stringValue.startswith("This")
    e = timer()
    print("Elapsed 1: %f seconds" % (e - s))


def efficiency_loop2():
    s = timer()
    for i in range(1,400000):
        stringValue[:len("This")] == ("This")
    e = timer()
    print("Elapsed 2: %f seconds" % (e - s))


def efficiency_loop3():
    s = timer()
    pattern = re.compile("^" + re.escape("This"))
    for i in range(1, 400000):
        bool(pattern.match(stringValue))
    e = timer()
    print("Elapsed 3: %f seconds" % (e - s))


def efficiency_loop4():
    s = timer()
    for i in range(1,400000):
        stringValue.endswith("big!")
    e = timer()
    print("Elapsed 1: %f seconds" % (e - s))


def efficiency_loop5():
    s = timer()
    for i in range(1,400000):
        stringValue[-len("big!"):] == ("big!")
    e = timer()
    print("Elapsed 2: %f seconds" % (e - s))


def efficient_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    return s[:i+1]


def efficiency_loop6(s):
    st = timer()
    for i in range(1, 400000):
        s.rstrip()
    e = timer()
    print("Elapsed 1: %f seconds" % (e - st))


def efficiency_loop7(s):
    st = timer()
    for j in range(1, 400000):
        efficient_rstrip(s)
    e = timer()
    print("Elapsed 2: %f seconds" % (e - st))


def efficient_hasattr(obj, attr_name):
    try:
        getattr(obj, attr_name)
        return True
    except AttributeError:
        return False


def efficiency_loop8():
    st = timer()
    for j in range(1, 400000):
        if(hasattr(obj, 'x')):
            ''
    e = timer()
    print("Elapsed 1: %f seconds" % (e - st))


def efficiency_loop9():
    st = timer()
    for j in range(1, 400000):
        if(efficient_hasattr(obj, 'x')):
            ''
    e = timer()
    print("Elapsed 2: %f seconds" % (e - st))

def efficiency_loop10():
    st = timer()
    hasAttrCheck=False
    for j in range(1, 400000):
        if(j==0):
            hasAttrCheck = hasattr(obj, 'x')
        if(hasAttrCheck):
            ''
    e = timer()
    print("Elapsed 3: %f seconds" % (e - st))

def efficiency_loop11():
    st = timer()
    for j in range(1, 400000):
        if type(my_ListObject) == (0b1000):
            ''
    e = timer()
    print("Elapsed 1: %f seconds" % (e - st))

def efficiency_loop12():
    st = timer()
    for j in range(1, 400000):
        if isinstance(my_ListObject, list):
            ''
    e = timer()
    print("Elapsed 2: %f seconds" % (e - st))

print("Starts with Tests: \n")
efficiency_loop1()
efficiency_loop2()
efficiency_loop3()
print("\nEnds with Tests: \n")
efficiency_loop4()
efficiency_loop5()
print("\nStrip Tests: \n")
efficiency_loop6(scut)
efficiency_loop7(scut)
print("\nHasAttr Tests: \n")
efficiency_loop8()
efficiency_loop9()
efficiency_loop10()
print("\nisInstance Tests: \n")
efficiency_loop11()
efficiency_loop12()