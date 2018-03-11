import pygame as pg
from .. import setup
from .. import constants as c

class Bad(pg.sprite.Sprite):
    """Flashing coin next to coin total info"""
    def __init__(self, x, y):
        super(Bad, self).__init__()
        self.sprite_sheet = setup.GFX['flashing_bad']
        self.create_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.first_half = True
        self.frame_index = 0
        
    def create_frames(self):
        """Extract coin images from sprite sheet and assign them to a list"""
        self.frames = []
        self.frame_index = 0

        self.frames.append(self.get_image(0, 0, 16, 36))  #black
        self.frames.append(self.get_image(23, 0, 20, 42))  #light
        
    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*2),
                                    int(rect.height*2)))
        return image
        
    def update(self, current_time):
        """Animates flashing bad"""
        if self.first_half:
            if self.frame_index == 0:
                if (current_time - self.timer) > 375:
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index == 1:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.timer = current_time
        else:
            if self.frame_index == 1:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.timer = current_time

        self.image = self.frames[self.frame_index]