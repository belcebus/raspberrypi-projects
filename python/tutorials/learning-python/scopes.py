#Local, Enclosing, Global, Built-in

def outter():
    test = 1
    def inner():
        global test 
        test = 2
        print("inner",test)
    inner()
    print("outter", test)

test = 0
outter()
print("global",test)


