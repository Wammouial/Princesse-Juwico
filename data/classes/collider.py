import pygame as pg
from .. import constants as c
from .. import setup

class Collider(pg.sprite.Sprite):
    """Invisible sprites placed overtop background parts
    that can be collided with (pipes, steps, ground, etc."""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        
class Collider_Level0 (pg.sprite.Sprite):
    """Visibles sprites for level0 when some ways are
    blocked"""
    
    def __init__(self,x,y,width,height,name='collider_level0'):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['blocs']
        self.setup_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        
    def setup_image(self):
        self.image = self.get_image(136,69,32,48)
    
    
    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        image = pg.transform.scale(image,
                                   (int(rect.width*2),
                                    int(rect.height*2)))

        return image
        
class Collider_Launcher (pg.sprite.Sprite):
    """Visibles sprites for level0 when some ways are
    blocked"""
    
    def __init__(self,x,y,width,height,name='collider_launcher'):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['collider_launcher']
        self.setup_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        
    def setup_image(self):
        self.image = self.get_image(0,4,60,140)
    
    
    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        return image
        
class Collider_Paysan (pg.sprite.Sprite):
    """Visibles sprites for level0 when some ways are
    blocked"""
    
    def __init__(self,x,y,width,height,name='end_paysan'):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['end_paysan']
        self.setup_image()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
        
    def setup_image(self):
        self.image = self.get_image(0,0,100,77)
    
    
    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        return image
        
