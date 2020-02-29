var1 = 50
var2 = 100

conta = (var1 + var2) * var1
print (conta)

def testes():
    def faz_conta():
        return 0

    def oi():
        print ('oi')
        print ('oi')


    def soma_dois_valores(valor1, valor2):
        return valor1 + valor2

    x = soma_dois_valores(3, 4)
    print(x)
    x = soma_dois_valores(2, 8)
    print(x)

    def raiz_quadrada(valor3):
       return valor3 ** (1/2)

    x = raiz_quadrada(9)
    print(x)

    def raiz(valor, base):
        return valor ** (1 / base)

    x = raiz(9, 2)
    print (x)

    def e_par(valor):
        return (valor % 2) == 0

    print(e_par(4))
    print(e_par(5))

    def div_por_seis(valor):
        return ((valor % 2) == 0) and ((valor% 3) == 0)

    print(div_por_seis(7))
    print(div_por_seis(9))
    print(div_por_seis(12))

def e_par(valor):
        return (valor % 2) == 0
def testa_par():
    '''Le um valor inserido pelo usuario, verifica se o valor é par e retorna uma mensagem'''
    parada = False
    while parada == False:
        valor = input('Insira um valor numérico, ou aperte ENTER para encerrar...\n')
        if valor == '':
            parada = True
        elif e_par(int(valor)) == True:
                print('O valor inserido é par.')
        else:
                print('O valor inserido é impar')

def dez_mult_tres():
    '''Imprime os primeiros 10 numeros não negativos multiplos de 3'''
    cont = 0
    numero = 1
    while cont < 10:
        if numero % 3 == 0:
            print(numero)
            cont += 1
        numero += 1

dez_mult_tres()



testa_par()

