
from domino import Domino

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

print(dominoes)

def not_in(deposited_indexes, i):
    for j in range(len(deposited_indexes)):
        if deposited_indexes[j] == i:
            return False
    return True

def deposits_domino(dominoes):
    deposited_dominoes = []
    deposited_indexes = []
    deposited_dominoes.append(dominoes[0])
    deposited_indexes.append(0)
    while len(deposited_dominoes) < len(dominoes):
        for i in range(1, len(dominoes)):
            if not_in(deposited_indexes, i):
                last_number = deposited_dominoes[-1].values[1]
                a = dominoes[i].values[0]
                b = dominoes[i].values[1]
                if a == last_number or b == last_number:
                    deposited_indexes.append(i)
                    if a == last_number:
                        deposited_dominoes.append(dominoes[i])
                    else:
                        deposited_dominoes.append(Domino(b, a))
    return deposited_dominoes

print(deposits_domino(dominoes))
