#Função
def c_f(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def f_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius