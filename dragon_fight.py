import arcade
import random
import os
import numpy
import df_story as story
import df_combat as comb

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 1000
HEIGHT = 600
TITLE = "Dragon Fight"
SPRITE_SCALING = 1

# Criação das classes de sprite que serão utilizadas no jogo

# def update faz com que os sprites se movam durante a execução do código,
# utilizando o centro dos sprites para determinar sua posição.
class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > WIDTH - 1:
            self.right = WIDTH - 1

        if self.bottom < 100:
            self.bottom = 100
            self.jumping = False
            self.can_jump = True

        elif self.top > HEIGHT - 1:
            self.top = HEIGHT - 1
    
    def setup(self):
        # Se alterar o __init__ da classe, não da para usar como arcade.sprite,
        # então foi feita essa função, para adicionar variáveis que botariamos no __init__
        
        self.PLAYER_MOVEMENT_SPEED = 5

        # Variáveis de controle do pulo
        self.jumping = False
        self.impulse = 0
        self.can_jump = True

        # Variáveis de controle do agachamento
        self.crouching = False
        self.can_crouch = True

        self.height = self.top - self.bottom


class Dragon(arcade.Sprite):
    
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        """if self.bottom != altura do chão:
            pass
            self.bottom = altura do chão """

    def setup(self, element):
        self.element = element


class Ground(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > HEIGHT - 1:
            self.top = HEIGHT - 1




# Classe que é responsável pela exibição do menu inicial do jogo
class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.ground_list = arcade.SpriteList()

        self.ground_sprite = Ground("images/ground.png", 1)
        self.ground_sprite.scale = 1
        self.ground_sprite.center_y = self.ground_sprite.height / 2
        self.ground_sprite.center_x = 0
        self.ground_list.append(self.ground_sprite)


        # Loop para fazer com que o chão ocupe a largura da tela inteira
        # no começo do jogo.

        difference = (self.ground_sprite.right - self.ground_sprite.left)

        while self.ground_list[-1].center_x <= WIDTH:
            self.new_ground = Ground('images/ground.png', 1)
            self.new_ground.bottom = 0
            self.new_ground.center_x = self.ground_list[-1].center_x + difference
            self.new_ground.scale = 1
            self.ground_list.append(self.new_ground) 

        """self.cloud_list = arcade.SpriteList()

        self.cloud_sprite = Cloud('images/nuvem.png', .7)
        self.cloud_sprite.center_y = 400
        self.cloud_sprite.left = WIDTH
        self.cloud_sprite.speed = 2
        self.cloud_list.append(self.cloud_sprite)"""

        


    def on_show(self):
        arcade.set_background_color(arcade.color.SKY_BLUE)


    def on_draw(self):
        arcade.start_render()

        self.ground_list.draw()

        arcade.draw_text("DRAGON FIGHT", WIDTH/2, HEIGHT/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Clique para jogar", WIDTH/2, HEIGHT/2-75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")


    def on_mouse_press(self, x, y, button, modifiers):
       
        game = story.Story()
        self.window.show_view(game)


    def update(self, delta_time):
        
        """if self.cloud_list[-1].right < WIDTH - 200:
            cloud_odds = random.randint(0,10)
            if cloud_odds == 0:
                cloud_scaling = random.randint(6,10)
                self.new_cloud = Cloud('images/nuvem.png', cloud_scaling / 7)
                self.new_cloud.center_y = random.randint(375, 450)
                self.new_cloud.left = WIDTH
                self.new_cloud.speed = random.randrange(3, 5)/2
                self.cloud_list.append(self.new_cloud)

            # Código responsável pela criação de novas nuvens dentro do jogo,
            # se a última nuvem a ser gerada passar de 200 pixels de distância
            # do seu ponto de origem, outra pode ser gerada após um intervalo
            # aleatório de tempo, o tamanho da nuvem e sua posição também são aleatórios

        for cloud in self.cloud_list:
            cloud.left -= cloud.speed
            if cloud.right < 0:
                cloud.kill() """
        pass

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    menu = MenuView()
    window.show_view(menu)
    arcade.run()


if __name__ == "__main__":
    main()