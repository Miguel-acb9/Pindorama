''' Bibliotaca Pindorama '''


# Importações de Bibliotecas e Módulos
import os
import sys
import pygame
from enum import Enum
from pygame.locals import *
from Pindorama.constantes import *


class Menu_Principal:
    ''' Menu Principal do Jogo'''
    def __init__(self):
        # Pygame
        pygame.init()
        self.relogio = pygame.time.Clock()
        pygame.display.set_caption(JOGO_NOME)
        self.tempo_primario = pygame.time.get_ticks()
        self.display = pygame.Surface((TELA_LARGURA, TELA_ALTURA))
        self.janela = pygame.display.set_mode((JANELA_LARGURA, JANELA_ALTURA))
        
        # Variáveis
        self.opt_menu = 0
        self.jogadorPosisao = [50, 50]
        self.opt_escolhida = 0
        self.movendoDireita = False
        self.movendoEsquerda = False
        self.jogadorPosisao = [50, 50]
        self.estado = Estado.menu_abertura
        if MODO_DESENVOLVEDOR:
            self.estado = Estado.menu_principal # Redirecionamento direto

    def gerenciador(self):
        ''' O gerenciador chama as funções da classe Pindorama() '''
        if self.estado == Estado.menu_abertura:
            self.menu_abertura()

        elif self.estado == Estado.menu_principal:
            self.menu_principal()

        elif self.estado == Estado.menu_jogar:
            self.menu_jogar()

        elif self.estado == Estado.menu_opcoes:
            self.menu_opcoes()

        elif self.estado == Estado.jogo_arena:
            self.jogo_arena()
    
    def menu_abertura(self):
        # Carregamento de Fontes
        fonte_h1 = pygame.font.Font('Fontes/alterebro-pixel-font.ttf', H1)
        fonte_h3 = pygame.font.Font('Fontes/alterebro-pixel-font.ttf', H3)
        txt_1 = fonte_h1.render('MacB', True, BRANCO)
        txt_2 = fonte_h3.render('Studio', True, BRANCO)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Lógica
        agora = pygame.time.get_ticks()
        if (agora - self.tempo_primario) >= 2000:
            self.estado = Estado.menu_principal

        # Desenho
        self.janela.fill((0, 40, 40))
        self.janela.blit(txt_1, txt_1.get_rect(center=(JANELA_LARGURA/2, -50 + JANELA_ALTURA/2)))
        self.janela.blit(txt_2, txt_2.get_rect(center=(JANELA_LARGURA/2, +50 + JANELA_ALTURA/2)))
          
    def menu_principal(self):
        # Fontes
        fundo = pygame.transform.scale(pygame.image.load('Imagens/fundo.jpg'), (JANELA_LARGURA, JANELA_ALTURA))
        fonte_h1 = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H1)
        fonte_h4 = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H4)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    self.opt_menu += 1
                    if self.opt_escolhida == 4:
                        if self.opt_menu > 1:
                            self.opt_menu = 1

                    else:
                        if self.opt_menu > 3:
                            self.opt_menu = 3

                if evento.key == K_UP:
                    self.opt_menu -= 1
                    if self.opt_escolhida == 4:
                        if self.opt_menu < 0:
                            self.opt_menu = 0
                    else:
                        if self.opt_menu < 0:
                            self.opt_menu = 0

                if evento.key == K_RETURN:
                    if self.opt_escolhida == 4:
                        if self.opt_menu == 0:
                            pygame.quit()
                            sys.exit()

                        elif self.opt_menu == 1:
                            self.opt_menu = 0
                            self.opt_escolhida = 0

                    else:
                        if self.opt_menu == 0:  # Menu Principal => Jogar
                            self.estado = Estado.menu_jogar

                        elif self.opt_menu == 1:  # Menu Principal => Opções
                            self.opt_menu = 0
                            self.estado = Estado.menu_opcoes

                        elif self.opt_menu == 2:  # Menu Principal => Créditos
                            self.opt_escolhida = 3

                        elif self.opt_menu == 3:  # Menu Principal => Sair
                            self.opt_menu = 0
                            self.opt_escolhida = 4

                if evento.key == K_ESCAPE:
                    if self.opt_escolhida == 0:  # Menu Principal
                        self.opt_menu = 0
                        self.opt_escolhida = 4

                    elif self.opt_escolhida == 3:  # Menu Principal => Créditos
                        self.opt_menu = 0
                        self.opt_escolhida = 0

                    elif self.opt_escolhida == 4:  # Menu Principal => Sair
                        self.opt_menu = 0
                        self.opt_escolhida = 0

        # Desenho
        self.janela.fill((0, 40, 40))
        self.janela.blit(fundo, (0, 0))
        if self.opt_escolhida == 0:  # Menu Principal
            # Textos
            txt_titulo = fonte_h1.render('Pindorama', True, BRANCO)
            txt_versao = fonte_h4.render(f'{JOGO_VERSAO}', True, BRANCO)
            txt_produtora = fonte_h4.render(f'@ 2021 - MacB, Studio', True, BRANCO)
            if self.opt_menu == 0:
                txt_menu_1 = fonte_h4.render('Jogar', True, CINZA)
                txt_menu_2 = fonte_h4.render('Opções', True, BRANCO)
                txt_menu_3 = fonte_h4.render('Créditos', True, BRANCO)
                txt_menu_4 = fonte_h4.render('Sair', True, BRANCO)
            
            elif self.opt_menu == 1:
                txt_menu_1 = fonte_h4.render('Jogar', True, BRANCO)
                txt_menu_2 = fonte_h4.render('Opções', True, CINZA)
                txt_menu_3 = fonte_h4.render('Créditos', True, BRANCO)
                txt_menu_4 = fonte_h4.render('Sair', True, BRANCO)
            
            elif self.opt_menu == 2:
                txt_menu_1 = fonte_h4.render('Jogar', True, BRANCO)
                txt_menu_2 = fonte_h4.render('Opções', True, BRANCO)
                txt_menu_3 = fonte_h4.render('Créditos', True, CINZA)
                txt_menu_4 = fonte_h4.render('Sair', True, BRANCO)

            elif self.opt_menu == 3:
                txt_menu_1 = fonte_h4.render('Jogar', True, BRANCO)
                txt_menu_2 = fonte_h4.render('Opções', True, BRANCO)
                txt_menu_3 = fonte_h4.render('Créditos', True, BRANCO)
                txt_menu_4 = fonte_h4.render('Sair', True, CINZA)

            # Desenho
            self.janela.blit(txt_titulo, txt_titulo.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_versao, txt_versao.get_rect(center=(JANELA_LARGURA - 40, JANELA_ALTURA - 30)))
            self.janela.blit(txt_produtora, txt_produtora.get_rect(center=(150, JANELA_ALTURA - 30)))
            self.janela.blit(txt_menu_1, txt_menu_1.get_rect(center=(JANELA_LARGURA/2, 350)))
            self.janela.blit(txt_menu_2, txt_menu_2.get_rect(center=(JANELA_LARGURA/2, 400)))
            self.janela.blit(txt_menu_3, txt_menu_3.get_rect(center=(JANELA_LARGURA/2, 450)))
            self.janela.blit(txt_menu_4, txt_menu_4.get_rect(center=(JANELA_LARGURA/2, 500)))
            if self.opt_menu == 0:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 350, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 350, 10, 10], 2)

            elif self.opt_menu == 1:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 400, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 400, 10, 10], 2)
            
            elif self.opt_menu == 2:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 450, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 450, 10, 10], 2)

            elif self.opt_menu == 3:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 500, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 500, 10, 10], 2)
        
        elif self.opt_escolhida == 3:  # Menu Principal => Créditos
            self.janela.fill((0, 40, 40))
            # Textos
            txt_titulo = fonte_h1.render('Créditos' , True , (255, 255, 255))
            txt_creditos1 = fonte_h4.render('Desenvolvidor' , True , (255, 255, 255))
            txt_creditos2 = fonte_h4.render('Miguel Alves Cordeiro Braz' , True , (255, 255, 255))

            # Desenho
            self.janela.blit(txt_titulo, txt_titulo.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_creditos1, txt_creditos1.get_rect(center=(JANELA_LARGURA/2, 350)))
            self.janela.blit(txt_creditos2, txt_creditos2.get_rect(center=(JANELA_LARGURA/2, 400)))
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])

        elif self.opt_escolhida == 4:  # Menu Principal => Sair
            self.janela.fill((0, 30, 30))
            fundo = pygame.transform.scale(pygame.image.load('Imagens/fundo.jpg'), (JANELA_LARGURA, JANELA_ALTURA))
            # Textos
            txt_titulo = fonte_h1.render('Pindorama', True, CINZA)
            txt_versao = fonte_h4.render(f'{JOGO_VERSAO}', True, CINZA)
            txt_produtora = fonte_h4.render(f'@ 2021 - MacB, Studio', True, CINZA)
            txt_sair = fonte_h4.render('Sair do Jogo?', True, BRANCO)
            if self.opt_menu == 0:
                txt_sair_sim = fonte_h4.render('Sim', True, CINZA)
                txt_sair_nao = fonte_h4.render('Não', True, BRANCO)

            elif self.opt_menu == 1:
                txt_sair_sim = fonte_h4.render('Sim', True, BRANCO)
                txt_sair_nao = fonte_h4.render('Não', True, CINZA)

            # Desenho
            self.janela.blit(fundo, (0,0))
            self.janela.blit(txt_titulo, txt_titulo.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_versao, txt_versao.get_rect(center=(JANELA_LARGURA - 40, JANELA_ALTURA - 30)))
            self.janela.blit(txt_produtora, txt_produtora.get_rect(center=(150, JANELA_ALTURA - 30)))
            self.janela.blit(txt_sair, txt_sair.get_rect(center=(JANELA_LARGURA/2, 350)))
            self.janela.blit(txt_sair_sim, txt_sair_sim.get_rect(center=(JANELA_LARGURA/2, 400)))
            self.janela.blit(txt_sair_nao, txt_sair_nao.get_rect(center=(JANELA_LARGURA/2, 450)))
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])
            if self.opt_menu == 0:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 400, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 400, 10, 10], 2)

            elif self.opt_menu == 1:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 450, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 450, 10, 10], 2)

    def menu_jogar(self):
        # Fontes
        titulo = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H1)
        texto = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H4)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    self.opt_menu += 1
                    if self.opt_menu > 1:
                        self.opt_menu = 1

                if evento.key == K_UP:
                    self.opt_menu -= 1
                    if self.opt_menu < 0:
                        self.opt_menu = 0

                if evento.key == K_ESCAPE:
                    if self.opt_escolhida != 0:
                        self.opt_menu = 0
                        self.opt_escolhida = 0

                    else:
                        self.estado = Estado.menu_abertura
                        self.opt_menu = 0
                        self.opt_escolhida = 0

                if evento.key == K_RETURN:
                    if self.opt_menu == 0:
                        self.opt_escolhida = 1 # Campanha 

                    elif self.opt_menu == 1:
                        self.estado = Estado.jogo_arena

        # Desenho
        self.janela.fill((0, 40, 40))
        if self.opt_escolhida == 0: # Menu Jogar
            # Texto
            txt_titulo = titulo.render('Jogar' , True , (255, 255, 255))
            if self.opt_menu == 0:
                txt_menu_1 = texto.render('Campanha' , True , (150, 150, 150))
                txt_menu_2 = texto.render('Arena' , True , (255, 255, 255))

            elif self.opt_menu == 1:
                txt_menu_1 = texto.render('Campanha' , True , (255, 255, 255))
                txt_menu_2 = texto.render('Arena' , True , (150, 150, 150))

            # Desenho
            self.janela.blit(txt_titulo, txt_titulo.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_menu_1, txt_menu_1.get_rect(center=(JANELA_LARGURA/2, 350)))
            self.janela.blit(txt_menu_2, txt_menu_2.get_rect(center=(JANELA_LARGURA/2, 400)))
            if self.opt_menu == 0:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 350, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 350, 10, 10], 2)

            elif self.opt_menu == 1:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 400, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 400, 10, 10], 2)
    
    def menu_opcoes(self):
        # Fontes
        fonte_h1 = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H1)
        fonte_h4 = pygame.font.Font("Fontes/alterebro-pixel-font.ttf", H4)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == KEYDOWN:
                if evento.key == K_DOWN:
                    self.opt_menu += 1
                    if self.opt_menu > 3:
                        self.opt_menu = 3

                if evento.key == K_UP:
                    self.opt_menu -= 1
                    if self.opt_menu < 0:
                        self.opt_menu = 0

                if evento.key == K_ESCAPE:
                    if self.opt_escolhida != 0:
                        self.opt_menu = 0
                        self.opt_escolhida = 0

                    else:
                        self.estado = Estado.menu_principal
                        self.opt_menu = 0
                        self.opt_escolhida = 0

                if evento.key == K_RETURN:
                    if self.opt_menu == 0:
                        self.opt_escolhida = 1

                    elif self.opt_menu == 1:
                        self.opt_escolhida = 2

                    elif self.opt_menu == 2:
                        self.opt_escolhida = 3

                    elif self.opt_menu == 3:
                        self.opt_escolhida = 4

        # Desenho
        self.janela.fill((0, 40, 40))
        if self.opt_escolhida == 0: # Menu Opções
            # Texto
            txt_titulo = fonte_h1.render('Opções' , True , (255, 255, 255))
            if self.opt_menu == 0:
                txt_menu_1 = fonte_h4.render('Jogo' , True , (150, 150, 150))
                txt_menu_2 = fonte_h4.render('Áudio' , True , (255, 255, 255))
                txt_menu_3 = fonte_h4.render('Vídeo' , True , (255, 255, 255))
                txt_menu_4 = fonte_h4.render('Controles' , True , (255, 255, 255))

            elif self.opt_menu == 1:
                txt_menu_1 = fonte_h4.render('Jogo' , True , (255, 255, 255))
                txt_menu_2 = fonte_h4.render('Áudio' , True , (255, 255, 255))
                txt_menu_3 = fonte_h4.render('Vídeo' , True , (150, 150, 150))
                txt_menu_4 = fonte_h4.render('Controles' , True , (255, 255, 255))

            elif self.opt_menu == 2:
                txt_menu_1 = fonte_h4.render('Jogo' , True , (255, 255, 255))
                txt_menu_2 = fonte_h4.render('Áudio' , True , (150, 150, 150))
                txt_menu_3 = fonte_h4.render('Vídeo' , True , (255, 255, 255))
                txt_menu_4 = fonte_h4.render('Controles' , True , (255, 255, 255))
            
            elif self.opt_menu == 3:
                txt_menu_1 = fonte_h4.render('Jogo' , True , (255, 255, 255))
                txt_menu_2 = fonte_h4.render('Áudio' , True , (255, 255, 255))
                txt_menu_3 = fonte_h4.render('Vídeo' , True , (255, 255, 255))
                txt_menu_4 = fonte_h4.render('Controles' , True , (150, 150, 150))

            # Desenho
            self.janela.blit(txt_titulo, txt_titulo.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_menu_1, txt_menu_1.get_rect(center=(JANELA_LARGURA/2, 350)))
            self.janela.blit(txt_menu_2, txt_menu_2.get_rect(center=(JANELA_LARGURA/2, 400)))
            self.janela.blit(txt_menu_3, txt_menu_3.get_rect(center=(JANELA_LARGURA/2, 450)))
            self.janela.blit(txt_menu_4, txt_menu_4.get_rect(center=(JANELA_LARGURA/2, 500)))
            if self.opt_menu == 0:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 350, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 350, 10, 10], 2)

            elif self.opt_menu == 1:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 400, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 400, 10, 10], 2)

            elif self.opt_menu == 2:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 450, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 450, 10, 10], 2)

            elif self.opt_menu == 3:
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 - 120, 500, 10, 10], 2)
                pygame.draw.rect(self.janela, (255, 255, 255), [JANELA_LARGURA/2 + 100, 500, 10, 10], 2)
        
        elif self.opt_escolhida == 1: # Menu Opções => Jogo
            txt_titulo1 = fonte_h1.render('Opções', True, CINZA)
            txt_titulo2 = fonte_h4.render('Jogo', True, BRANCO)
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])
            self.janela.blit(txt_titulo1, txt_titulo1.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_titulo2, txt_titulo2.get_rect(center=(JANELA_LARGURA/2, 350)))

        elif self.opt_escolhida == 2: # Menu Opções => Vídeo
            txt_titulo1 = fonte_h1.render('Opções', True, CINZA)
            txt_titulo2 = fonte_h4.render('Vídeo', True, BRANCO)
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])
            self.janela.blit(txt_titulo1, txt_titulo1.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_titulo2, txt_titulo2.get_rect(center=(JANELA_LARGURA/2, 350)))

        elif self.opt_escolhida == 3: # Menu Opções => Áudio
            txt_titulo1 = fonte_h1.render('Opções', True, CINZA)
            txt_titulo2 = fonte_h4.render('Áudio', True, BRANCO)
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])
            self.janela.blit(txt_titulo1, txt_titulo1.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_titulo2, txt_titulo2.get_rect(center=(JANELA_LARGURA/2, 350)))
            
        elif self.opt_escolhida == 4: # Menu Opções => Controles
            txt_titulo1 = fonte_h1.render('Opções', True, CINZA)
            txt_titulo2 = fonte_h4.render('Controles', True, BRANCO)
            pygame.draw.rect(self.janela, (255, 255, 255), [350, 353, 170, 3])
            pygame.draw.rect(self.janela, (255, 255, 255), [755, 353, 170, 3])
            self.janela.blit(txt_titulo1, txt_titulo1.get_rect(center=(JANELA_LARGURA/2, 150)))
            self.janela.blit(txt_titulo2, txt_titulo2.get_rect(center=(JANELA_LARGURA/2, 350)))

    def jogo_campanha(self):
        ''' x '''
        pass
    
    def jogo_arena(self):
        ''' x '''
        img_jogador = pygame.image.load('Imagens/player.png')
        # Eventos
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == KEYDOWN:
                if evento.key == K_RIGHT:
                    self.movendoDireita = True

                if evento.key == K_LEFT:
                    self.movendoEsquerda = True

            if evento.type == KEYUP:
                if evento.key == K_RIGHT:
                    self.movendoDireita = False

                if evento.key == K_LEFT:
                    self.movendoEsquerda = False

        # Lógica
        if self.movendoDireita:
            self.jogadorPosisao[0] += 3

        if self.movendoEsquerda:
            self.jogadorPosisao[0] -= 3

        # Desenho
        self.janela.fill((0, 40, 40))
    
        self.janela.blit(img_jogador, self.jogadorPosisao)
