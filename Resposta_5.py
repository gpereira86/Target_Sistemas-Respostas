# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


def inverter_string(s):
    string_invertida = ''
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

s = input("Informe uma string para ver seu inverso: ")
print(f"String invertida: {inverter_string(s)}")