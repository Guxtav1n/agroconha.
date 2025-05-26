import pygame
import sys
from player import Player
from obstacles import Obstacles
from powerups import PowerUps

class CorridaCampoCidade:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Corrida do Campo à Cidade")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        # Cores temáticas
        self.colors = {
            'background': (30, 145, 65),  # Verde campo
            'city': (70, 70, 70),         # Cinza cidade
            'text': (255, 215, 0)        # Dourado
        }
        
        # Carrega assets
        self.load_assets()
        
        # Cria jogador
        self.player = Player()
        self.obstacles = Obstacles()
        self.powerups = PowerUps()
        
        # Estado do jogo
        self.game_state = "running"  # running, paused, game_over
        self.score = 0
        self.distance = 0
    
    def load_assets(self):
        """Carrega imagens, sons e outros recursos"""
        try:
            # Aqui você carregaria os assets reais
            self.backgrounds = {
                'campo': pygame.Surface((800, 600)),
                'cidade': pygame.Surface((800, 600))
            }
            # Preenche com cores temporárias
            self.backgrounds['campo'].fill(self.colors['background'])
            self.backgrounds['cidade'].fill(self.colors['city'])
            
        except Exception as e:
            print(f"Erro ao carregar assets: {e}")
            sys.exit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = "paused" if self.game_state == "running" else "running"
        
        return True
    
    def update(self):
        if self.game_state != "running":
            return
            
        self.distance += 1
        self.score = self.distance // 10
        
        # Transição de campo para cidade
        background_index = min(self.distance // 1000, 1)
        
        self.player.update()
        self.obstacles.update()
        self.powerups.update()
        
        # Verifica colisões
        self.check_collisions()
    
    def check_collisions(self):
        # Implementar lógica de colisão
        pass
    
    def render(self):
        # Renderiza o fundo com base na distância
        background_index = min(self.distance // 1000, 1)
        self.screen.blit(self.backgrounds['campo' if background_index == 0 else 'cidade'], (0, 0))
        
        # Renderiza elementos do jogo
        self.player.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.powerups.draw(self.screen)
        
        # Renderiza UI
        score_text = self.font.render(f"Pontuação: {self.score}", True, self.colors['text'])
        self.screen.blit(score_text, (10, 10))
        
        if self.game_state == "paused":
            pause_text = self.font.render("PAUSADO", True, (255, 255, 255))
            self.screen.blit(pause_text, (400 - pause_text.get_width()//2, 300))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    game = CorridaCampoCidade()
    game.run()
    pygame.quit()
    sys.exit()
