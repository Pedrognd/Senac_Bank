# DIVISORIA NO CONSOLE #
def ajustar():
    print('+' + '='*48 + '+')

# LIMPAR CONSOLE #
def cls():
    import os
    os.system('cls') or None

# GERAR CODIGO DE CONTA #
def GerCod():
    from string import digits 
    from random import choice
    valores = digits # 0123456789 #
    senha = ''
    for i in range(3):
        senha += choice(valores)

    return senha

# TIMER DE ESPERA PARA OUTRO METODO #
def espera(tp):
    from time import sleep as sp
    sp(tp)

