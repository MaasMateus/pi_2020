import arcade
import random
import os
import numpy


file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 1000
HEIGHT = 600
TITLE = "Dragon Fight"
SPRITE_SCALING = 1

class Story(arcade.View):

    def __init__(self):
        super().__init__()        

    
    def on_show(self):
        arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, arcade.color.BLACK)
            


    def on_draw(self):
        
        arcade.draw_text("DRAGON FIGHT", WIDTH/2, HEIGHT/2,
                         (255,255,255), font_size= 50, anchor_x="center")
    
    
    def update(self, delta_time):
        pass

    
    def on_mouse_press(self, x, y, button, modifiers):    
        story = MainTitle()
        self.window.show_view(story)

class MainTitle(arcade.View):
    
    def __init__(self):
        super().__init__()
        self.font_size = 50
        self.r = 255
        self.g = 255
        self.b = 255

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    
    
    def on_draw(self):
        arcade.draw_text("DRAGON FIGHT", WIDTH/2, HEIGHT/2,
                         (self.r,self.g,self.b), font_size=self.font_size, anchor_x="center")

    
    def update(self, delta_time):
        arcade.set_background_color(arcade.color.BLACK)
        if self.font_size < 80:
            arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, arcade.color.BLACK)
            self.font_size += 2
        
        elif self.r > 0:
            arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, arcade.color.BLACK)
            self.font_size += 2
            self.r -= 15
            self.g -= 15
            self.b -= 15
            
            
        

def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    story = Story()
    window.show_view(story)
    arcade.run()


if __name__ == "__main__":
    main()