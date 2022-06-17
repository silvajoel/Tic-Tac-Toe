def verifica_ganhador():
    # Checando linhas
    for i in range(tam):
        soma = matriz[i][0] + matriz[i][1] + matriz[i][2]
        if soma == 3 or soma == -3:
            return 1
    # Checando colunas
    for i in range(tam):
        soma = matriz[0][i], matriz[1][i], matriz[2][i]
        if soma == 3 or soma == -3:
            return 1

    # Checando diagonais

    diagonal_1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    diagonal_2 = matriz[0][2] + matriz[1][1] + matriz[2][0]

    if diagonal_1 == 3 or diagonal_1 == -3 or diagonal_2 == 3 or diagonal_2 == -3:
        return 1

    return 0


def printa_matriz():

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                print("[   ]", end=' ')
            elif matriz[i][j] == 1:
                print("[ X ]", end=' ')
            elif matriz[i][j] == -1:
                print("[ O ]", end=' ')
        print()

def game():

    jogadas = 0

    while verifica_ganhador() == 0:

        print("\nJogador ", jogadas%2 + 1)
        print('Digite a linha e coluna:')
        printa_matriz()
        linha = int(input())
        coluna = int(input())

        if matriz[linha][coluna] == 0:
            if jogadas %2 != 0:
                matriz[linha][coluna] = 1
                jogadas = jogadas + 1
            else:
                matriz[linha][coluna] = -1
                jogadas = jogadas + 1
        else:
            print("Está posição não está vazia!")
            jogadas = jogadas - 1

        if verifica_ganhador() == 1:
            print('Você ganhou!!')
            printa_matriz()
            break
        if (jogadas>=9):
            print("Empate!")
            break

    jogadas = jogadas + 1
    
if __name__ == '__main__':
    op = 0

    tam = 3
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while op != 3:
        print('-=' * 5 + ' TIC TAC TOE ' + '=-' * 5)
        print('\n[ 1 ] Jogar \n[ 2 ] Como jogar \n[ 3 ] Sair')
        op = int(input())

        if op == 1:
            game()
