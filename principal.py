''' Pindorama '''


# Importações de Bibliotecas e Módulos
from Pindorama.constantes import *
from Pindorama.menu_principal import *


def principal():
    ''' Loop do Menu Principal do Jogo '''
    menu = Menu_Principal()
    while True:
        menu.gerenciador()
        pygame.display.update()
        menu.relogio.tick(FPS)


if __name__ == '__main__':
    principal()