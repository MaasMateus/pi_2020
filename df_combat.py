import arcade
import random
import os
import numpy

# elementos: eletrico, terra, agua e fogo
# lista de críticos: da crit > sofre crit
# agua(8) > fogo(4) > terra(2) > eletrico(1) > agua...
# cada elemento possui um valor, se o valor do atacante dividido pelo do defensor for 2,
# o ataque realizado será crítico, se for 1/2, será fraco e se não for nenhum, será normal
# o elemento elétrico requer uma analise diferente para determinar o dano. 
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

def attack(element_atk, element_def, attack_dmg):
    crit = element_atk / element_def
    if crit == 2 or crit == (1/8):
        return attack_dmg * 2
    elif crit == .5 or crit == 8:
        return  int(round(attack_dmg / 2))
    return attack_dmg


def main():
    print(attack(4,8, 103))


if __name__ == "__main__":
    main()    




WIDTH = 1000
HEIGHT = 600
TITLE = "Dragon Fight"
SPRITE_SCALING = 1


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()