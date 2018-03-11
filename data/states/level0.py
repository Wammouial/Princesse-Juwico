import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. import game_sound
from .. classes import juwico_0
from .. classes import collider
from .. classes import info
from .. classes import score

class Level0(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        
    def startup(self, current_time, persist):
    
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.LEVEL_STATE] = c.NOT_FROZEN
        
        self.game_info[c.JUWICO_DEAD] = False
        
        if self.game_info[c.LEVEL_NUMBER] == '0-0' or self.game_info[c.LEVEL_NUMBER] == '0-1':   #En fonction du niveau précédent
            self.game_info[c.LEVEL_NUMBER] = '0-1'
            self.moment = 1
        elif self.game_info[c.LEVEL_NUMBER] == '1-1':
            self.game_info[c.LEVEL_NUMBER] = '0-2'
            self.moment = 2
        elif self.game_info[c.LEVEL_NUMBER] == '1-2':
            self.game_info[c.LEVEL_NUMBER] = '0-3'
            self.moment = 3
        elif self.game_info[c.LEVEL_NUMBER] == '1-3':
            self.game_info[c.LEVEL_NUMBER] = '0-4'
            self.moment = 4
        elif self.game_info[c.LEVEL_NUMBER] == '1-4':
            self.game_info[c.LEVEL_NUMBER] = '0-5'
            self.moment = 5
        
        
        
        self.state = c.NOT_FROZEN
        
        self.overhead_info_display = info.OverheadInfo(self.game_info, c.LEVEL0)
        self.sound_manager = game_sound.Sound(self.overhead_info_display)
        
        self.setup_juwico()
        self.setup_background()
        self.setup_steps()
        
        self.setup_parts()
        self.setup_spritegroups()
        
        
    def setup_background(self):
        """Sets the background image, rect and scales it to the correct proportions"""
        self.background = setup.GFX['level_0']
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height
        
        self.level = pg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom=self.level_rect.bottom)  
        self.viewport.x = self.game_info[c.CAMERA_START_X]  
        self.viewport = pg.Rect(800,600,800,600)
        
    def setup_juwico(self):
        """Places Juwico at the beginning of the level"""
        self.juwico = juwico_0.Juwico_0()
        self.juwico.rect.x =  900
        self.juwico.rect.bottom = 900
        
    def setup_steps(self): 
        """Create collideable rects for all the level"""
        step1 = collider.Collider(0,0,800,600)
        step2 = collider.Collider(1600,0,800,600)
        step3 = collider.Collider(0,1200,800,600)
        step4 = collider.Collider(1600,1200,800,600)
        
        step5 = collider.Collider(800,1200,323,254)
        step6 = collider.Collider(1311,1200,289,293)
        step7 = collider.Collider(1311,1200,289,293)
        step8 = collider.Collider(800,1584,348,216)

        step9 = collider.Collider(0,600,426,267)
        step10 = collider.Collider(0,928,426,271)
        step11 = collider.Collider(506,928,294,272)
        step12 = collider.Collider(506,600,294,267)
        
        step13 = collider.Collider(800,600,300,75)
        step14 = collider.Collider(1225,600,375,75)
        step15 = collider.Collider(1525,675,75,169)
        step16 = collider.Collider(1525,975,75,150)
        step17 = collider.Collider(1294,1125,306,75)
        step18 = collider.Collider(800,1125,381,75)
        step19 = collider.Collider(800,975,75,150)
        step20 = collider.Collider(800,675,75,150)
        
        step21 = collider.Collider(800,-200,1400,200)
        step22 = collider.Collider(2400,600,200,600)
        step23 = collider.Collider(800,1800,800,200)
        step24 = collider.Collider(-200,600,200,600)

        self.step_group = pg.sprite.Group(step1,  step2,
                                          step3,  step4,
                                          step5,  step6,
                                          step7,  step8,
                                          step9,  step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19, step20,
                                          step21, step22,
                                          step23, step24)

                                          
    def setup_spritegroups(self):
        """Sprite groups created for convenience"""
        self.ground_step_pipe_group = pg.sprite.Group(self.step_group,self.tree_group)
        self.juwico_group = pg.sprite.Group(self.juwico)
        
    def setup_parts(self):
        """"""
        if self.moment == 1:
            self.viewport1 = self.viewport
            self.viewport2 = pg.Rect(800,0,800,600)
            self.viewport_list = [self.viewport1, self.viewport2]
            self.create_colliders()
            
        elif self.moment == 2:
            self.viewport1 = self.viewport
            self.viewport2 = pg.Rect(0,600,800,600)
            self.viewport_list = [self.viewport1, self.viewport2]
            self.create_colliders()
        
        elif self.moment == 3:
            self.viewport1 = self.viewport
            self.viewport2 = pg.Rect(1600,600,800,600)
            self.viewport_list = [self.viewport1, self.viewport2]
            self.create_colliders()
            
        elif self.moment == 4:
            self.viewport1 = self.viewport
            self.viewport2 = pg.Rect(800,1200,800,600)
            self.viewport_list = [self.viewport1, self.viewport2]
            self.create_colliders()
        
        elif self.moment == 5:
            self.viewport1 = self.viewport
            self.viewport2 = self.viewport
            self.viewport_list = [self.viewport1, self.viewport2]
            self.create_colliders()
            
    def create_colliders(self):
        """"""
        left_tree = collider.Collider_Level0(800,854,79,93)
        right_tree = collider.Collider_Level0(1526,849,68,104)
        top_tree = collider.Collider_Level0(1122,605,90,100)
        bot_tree = collider.Collider_Level0(1196,1098,73,99)
        
        top_bad = collider.Collider_Launcher(1150,28,60,140)
        left_bad = collider.Collider_Launcher(17,815,60,140)
        right_bad = collider.Collider_Launcher(2247,826,60,140)
        bot_bad = collider.Collider_Launcher(1195,1650,60,140)
        
        paysan = collider.Collider_Paysan(1368,711,100,77)
        
        if self.moment == 1:
            self.tree_group = pg.sprite.Group(left_tree,right_tree,bot_tree)
            self.bad_group = pg.sprite.Group(top_bad)
        elif self.moment == 2:
            self.tree_group = pg.sprite.Group(top_tree,right_tree,bot_tree)
            self.bad_group = pg.sprite.Group(left_bad)
        elif self.moment == 3:
            self.tree_group = pg.sprite.Group(top_tree,left_tree,bot_tree)
            self.bad_group = pg.sprite.Group(right_bad)
        elif self.moment == 4:
            self.tree_group = pg.sprite.Group(top_tree,left_tree,right_tree)
            self.bad_group = pg.sprite.Group(bot_bad)
        elif self.moment == 5:
            self.tree_group = pg.sprite.Group(top_tree,left_tree,bot_tree,right_tree)
            self.bad_group = pg.sprite.Group(paysan)
        
    def update(self, surface, keys, current_time):
        """Updates Entire level using states.  Called by the control object"""
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.verif_viewport()
        self.verif_bad()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_info, self.juwico)
        
    
    def handle_states(self, keys):
        """If the level is in a FROZEN state, only juwico will update"""
        if self.state == c.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == c.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif keys[pg.K_ESCAPE]:
            self.end_game()
            
    def verif_viewport(self):
        """"""
        if self.viewport_list[1].contains(self.juwico.rect):
            self.viewport = self.viewport_list[1]
        elif self.viewport_list[0].contains(self.juwico.rect):
            self.viewport = self.viewport_list[0]
            
    def verif_bad(self):
        
        go_bad = pg.sprite.spritecollideany(self.juwico, self.bad_group)
        if go_bad:
            
            if self.moment == 1:
                self.next = c.LEVEL1
            elif self.moment ==2:
                self.next = c.LEVEL2
            elif self.moment == 3:
                self.next = c.LEVEL3
            elif self.moment == 4:
                self.next = c.LEVEL4
            elif self.moment == 5:
                self.next = c.END5
                
            self.end_game()
        
     
    def update_all_sprites(self, keys):
        """Updates the location of all sprites on the screen."""
        self.juwico.update(keys, self.game_info)
        self.adjust_sprite_positions()
        self.overhead_info_display.update(self.game_info, self.juwico)
            
    def adjust_sprite_positions(self):
        """Adjusts sprites by their x and y velocities and collisions"""
        self.adjust_juwico_position()
        
    def adjust_juwico_position(self):
        """Adjusts Juwico's position based on his x, y velocities and
        potential collisions"""
        self.last_x_position = self.juwico.rect.right
        self.last_y_position = self.juwico.rect.bottom
        
        self.juwico.rect.x += round(self.juwico.x_vel)
        
        
        self.check_juwico_x_collisions()
        
        self.juwico.rect.y += round(self.juwico.y_vel)
        self.check_juwico_y_collisions()
            
    def check_juwico_x_collisions(self):
        """Check for collisions after Juwico is moved on the x axis"""
        collider = pg.sprite.spritecollideany(self.juwico, self.ground_step_pipe_group)
        if collider:
            self.adjust_juwico_for_x_collisions(collider)
    
    def adjust_juwico_for_x_collisions(self, collider):
        """Puts Juwico flush next to the collider after moving on the x axis"""
        if self.juwico.rect.x < collider.rect.x:
            self.juwico.rect.right = collider.rect.left
        elif self.juwico.rect.x > collider.rect.x:
            self.juwico.rect.left = collider.rect.right

        self.juwico.x_vel = 0
        
    def check_juwico_y_collisions(self):
        """Checks for collisions when Juwico moves along the y-axis"""
        ground_step_or_pipe = pg.sprite.spritecollideany(self.juwico, self.ground_step_pipe_group)

        if ground_step_or_pipe:
            self.adjust_juwico_for_y_ground_pipe_collisions(ground_step_or_pipe)
    
    def adjust_juwico_for_y_ground_pipe_collisions(self, collider):  #A modifier
        """Juwico collisions with pipes on the y-axis"""
        if collider.rect.bottom > self.juwico.rect.bottom:
            self.juwico.y_vel = 0
            self.juwico.rect.bottom = collider.rect.top-1
            
        elif collider.rect.top < self.juwico.rect.top:
            self.juwico.y_vel = 0
            self.juwico.rect.top = collider.rect.bottom+1
            
    def end_game(self):
        """End the game"""
        self.sound_manager.stop_music()
        self.done = True
            
    
    def blit_everything(self, surface):
        """Blit all sprites to the main surface"""
        self.level.blit(self.background, self.viewport, self.viewport)
        #self.step_group.draw(self.level)
        self.juwico_group.draw(self.level)
        self.tree_group.draw(self.level)
        self.bad_group.draw(self.level)

        surface.blit(self.level, (0,0), self.viewport)
        self.overhead_info_display.draw(surface)
		