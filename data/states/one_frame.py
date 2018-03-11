import pygame as pg
import time
from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..classes import info

class Help(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()  #?

        self.overhead_info = info.OverheadInfo(self.game_info, info_state) #?
        self.sound_manager = game_sound.Sound(self.overhead_info)  #?
        
    def set_next_state(self):
        """Sets the next state"""
        return c.MAIN_MENU
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['help']
        return image
        
class End1(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        self.sfx_dict = setup.MUSIC
        pg.mixer.music.load(self.sfx_dict['end1'])
        pg.mixer.music.play()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)
        
    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL0
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            pg.mixer.music.stop()
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['end1']
        return image

class End2(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        self.sfx_dict = setup.MUSIC
        pg.mixer.music.load(self.sfx_dict['end2'])
        pg.mixer.music.play()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)
        
    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL0
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            pg.mixer.music.stop()
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['end2']
        return image
        
class End3(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        self.sfx_dict = setup.MUSIC
        pg.mixer.music.load(self.sfx_dict['end3'])
        pg.mixer.music.play()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)
        
    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL0
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            pg.mixer.music.stop()
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['end3']
        return image
        
class End4(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        self.sfx_dict = setup.MUSIC
        pg.mixer.music.load(self.sfx_dict['end4'])
        pg.mixer.music.play()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)
        
    def set_next_state(self):
        """Sets the next state"""
        return c.LEVEL0
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            pg.mixer.music.stop()
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['end4']
        return image
        
class End5(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
        
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        
        self.sfx_dict = setup.MUSIC
        pg.mixer.music.load(self.sfx_dict['end5'])
        pg.mixer.music.play()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)
        
    def set_next_state(self):
        """Sets the next state"""
        return c.MAIN_MENU
        
    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.MAIN_MENU
        
    
    
    def update(self, surface,keys, current_time):
        """Updates the loading screen"""
        
        surface.blit(self.get_image(),(0,0))
        self.update_frame(keys)
            
    def update_frame(self, keys):
        """Update the position of the cursor"""
        input = pg.K_SPACE
        skip = pg.K_ESCAPE
        
        if keys[input] or keys[skip]:
            pg.mixer.music.stop()
            self.done = True
                
    def get_image(self):
        """Returns images from intro"""
        image = setup.GFX['end5']
        return image