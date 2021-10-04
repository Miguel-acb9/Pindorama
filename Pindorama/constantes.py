''' Constantes de Pindorama '''


# Importações de Bibliotecas e Módulos
from enum import Enum


# Variáveis do Jogo
FPS                = 60
JOGO_VERSAO        = '0.1.3'
JOGO_NOME          = 'Pindorama'
MODO_DESENVOLVEDOR = False


# Tamanho dos Displays
TELA_ALTURA    = 240
TELA_LARGURA   = 360
JANELA_ALTURA  = 720
JANELA_LARGURA = 1280


# Cores(RGB)
ROXO     = (255,   0, 255)
AZUL     = (  0,   0, 255)
CINZA    = (150, 150, 150)
PRETO    = (  0,   0,   0)
CIANO    = (  0, 255, 255)
VERDE    = (  0, 255,   0)
BRANCO   = (255, 255, 255)
AMARELO  = (255, 255,   0)
VERMELHO = (255,   0,   0)


# Tamanho das Fontes
H1 = 200
H2 = 150
H3 = 100
H4 = 50
H5 = 25
H6 = 12

# Enumerações
class Estado(Enum):
    (menu_abertura,
    menu_principal,
    menu_jogar,
    menu_opcoes,
    jogo_campanha,
    jogo_arena) = range(6)