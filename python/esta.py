# No trecho de código fornecido, a variável SOMA está sendo incrementada com os valores de K, 
# onde K varia de 1 até o valor de INDICE, que é 13. Assim, a cada iteração, SOMA recebe o valor de SOMA + K.Portanto,
# ao final do processamento, o valor da variável SOMA será a soma dos números de 1 a 13, ou seja,
# SOMA será igual a 91.
# Este código calcula a soma dos números de 1 a INDICE.

INDICE = 13
SOMA = 0
K = 0

# Loop para somar os números de 1 a INDICE
while K < INDICE:
    K += 1
    SOMA += K

# Imprimir o resultado
print("O valor da variável SOMA é:", SOMA)


# Este código verifica se um número pertence à sequência de Fibonacci.

def verifica_fibonacci(num):
    # 
    # Verifica se um número pertence à sequência de Fibonacci.
    # Argumentos:
    #     num: O número a ser verificado.
    # Retorna:
    #     True se o número pertence à sequência de Fibonacci, False caso contrário.
    # 
    # Define as variáveis a e b com os valores 0 e 1, respectivamente.
    a, b = 0, 1

    # Entra em um loop while enquanto b for menor que o número passado como parâmetro.
    while b < num:
        # Troca os valores de a e b.
        a, b = b, a + b

    # Retorna True se b for igual ao número passado como parâmetro.
    if b == num:
        return True

    # Caso contrário, retorna False.
    else:
        return False


# Entrada de dados.
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Chamada da função.
if verifica_fibonacci(numero):
    # Imprime uma mensagem informando que o número pertence à sequência de Fibonacci.
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    # Imprime uma mensagem informando que o número não pertence à sequência de Fibonacci.
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

# a) A lógica é adicionar 2 a cada número anterior: 1, 3, 5, 7, 9...
# b) A lógica é multiplicar cada número anterior por 2: 2, 4, 8, 16, 32, 64, 128...
# c) A lógica é elevar ao quadrado o índice do número: 0, 1, 4, 9, 16, 25, 36, 49...
# d) A lógica é elevar o índice ao quadrado: 4, 16, 36, 64, 100...
# e) A lógica é a soma dos dois números anteriores na sequência de Fibonacci: 1, 1, 2, 3, 5, 8, 13...
# f) A lógica é somar 2 ao primeiro número, depois somar 6, depois somar 4, depois somar 2, e assim por diante: 2, 10, 12, 16, 17, 18, 19, 20...

# Uma possível solução para descobrir qual interruptor controla cada lâmpada usando apenas duas idas até uma das salas das lâmpadas seria seguir os seguintes passos:

# Ligue o primeiro interruptor e deixe-o ligado por alguns minutos.
# Depois, desligue o primeiro interruptor e ligue o segundo interruptor.
# Entre na sala das lâmpadas.
# A lâmpada acesa estará conectada ao interruptor que foi ligado e desligado.
# A lâmpada que está quente, mas apagada, estará conectada ao interruptor que foi ligado.
# Dessa forma, é possível determinar qual interruptor controla cada lâmpada.
    
# Este código inverte os caracteres de uma string.

def inverte_string(s):

    # Inverte os caracteres de uma string.

    # Argumentos:
    #     s: A string a ser invertida.

    # Retorna:
    #     A string invertida.8
    # Cria uma string vazia para armazenar a string invertida.
    reversed_string = ''

    # Itera sobre cada caractere na string original.
    for char in s:
        # Adiciona o caractere atual ao início da string invertida.
        reversed_string = char + reversed_string

    # Retorna a string invertida.
    return reversed_string


# Solicita ao usuário que digite uma string.
string = input("Digite uma string para ser invertida: ")

# Inverte a string usando a função `inverte_string`.
string_invertida = inverte_string(string)

# Imprime a string original e a string invertida.
print(f"String original: {string}")
print(f"String invertida: {string_invertida}")