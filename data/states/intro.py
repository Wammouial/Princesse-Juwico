import pygame as pg
import time
from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..classes import info

class Intro(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        self.frame = 1
        self.yesno = False
        pg.time.wait(1200)

        info_state = self.set_overhead_info_state() 

        self.overhead_info = info.OverheadInfo(self.game_info, info_state) 
        self.sound_manager = game_sound.Sound(self.overhead_info)  
        
    def set_next_state(self):
        """Sets the next state"""
        return c.LOAD_SCREEN
        
    def set_overhead_info_state(self): 
        """sets the state to send to the overhead info object"""
        return c.INTRO
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        list_surfaces_intro = self.get_image()
        
        if self.frame == 1:
            surface.blit(list_surfaces_intro[0],(0,0))
        elif self.frame == 2:
            surface.blit(list_surfaces_intro[1],(0,0))
        elif self.frame == 3:
            surface.blit(list_surfaces_intro[2],(0,0))
        elif self.frame == 4:
            surface.blit(list_surfaces_intro[3],(0,0))
        elif self.frame == 5:
            surface.blit(list_surfaces_intro[4],(0,0))
        elif self.frame == 6:
            surface.blit(list_surfaces_intro[5],(0,0))
        else:
            self.done = True
            
        
            
        self.update_frame(keys)
        
            
        if self.yesno == True:
            pg.time.wait(1500)
            keys = []
            self.yesno = False
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if self.frame < 7 :
            
            if keys[input]:
                self.frame += 1
                self.yesno = True
                keys = []
                
            elif keys[skip]:
                self.done = True
               
        
        else:
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        
        letter = "F"
        list_surfaces_intro = []
        
        for crement in range (1,7):
            
            name_file = letter + str(crement)
            current_image = setup.GFX[name_file]
            list_surfaces_intro.append(current_image)
            
        return list_surfaces_intro