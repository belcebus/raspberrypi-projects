def func(a,b,c):
    print(a,b,c)

# posicional
func("a","b","c")

# keyword
func(c="c",b="b",a="a")

# default values
def func_default_values(a,b="x",c="x"):
    print(a,b,c)

func_default_values("a")
func_default_values(a="a",c="c")

# variable argument number

def func_variable_arg_num(* n):
    #n es una tupla
    print(n)

func_variable_arg_num(1,2,3,4,5,5)

# variable keyword

def func_variable_arg_keyword(**kwargs):
    #kwargs (KeyWordArguments) es un diccionario
    
    argumentos={
        "a": kwargs.get("a",'default-a-value'),
        "b": kwargs.get("b",'default-b-value'),
        "fulanito": kwargs.get("fulanito",'default-fulanito-value')
    }
    print(kwargs, "->", argumentos)

func_variable_arg_keyword()
func_variable_arg_keyword(a=1,b=2,fulanito="34")
func_variable_arg_keyword(**{'a':1, 'd':4, 'fulanito':"34"})
func_variable_arg_keyword(** dict(a=1, b=2, fulanito="34"))
func_variable_arg_keyword(a=0)

# keyword only
def kwo1(*a,c):
    print(a,c)

kwo1("Hola","hola",c="Caracola")

def kwo2(a,b,*,c):
    print(a,b,c)

kwo2("Hola","hola",c="Caracola")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

for n in range(1,10):
    print(factorial(n))

def multiplication(a,b):
    """aprovechamos para retornar los atributos especiales"""
    return a*b

special_attributes = [ "__doc__", "__name__", "__qualname__", "__module__", "__defaults__", "__code__", "__globals__", "__dict__", "__closure__", "__annotations__", "__kwdefaults__", ]

for att in special_attributes:
    print(att, "->", getattr(multiplication, att))

