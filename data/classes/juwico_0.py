import pygame as pg
from .. import setup, tools
from .. import constants as c

class Juwico_0 (pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['princes']

        self.setup_timers()
        self.setup_state_booleans()
        self.setup_forces()
        self.setup_counters()
        self.load_images_from_sheet()

        self.state = c.WALK
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        self.key_timer = 0
        
    def setup_timers(self):
        """Sets up timers for animations"""
        self.walking_timer = 0
        
    def setup_state_booleans(self):
        """Sets up booleans that affect Juwico's behavior"""
        self.facing_right = True
        self.facing_up = False
        self.facing_down = False
        self.dead = False
        
        
    def setup_forces(self):
        """Sets up forces that affect Juwico's velocity"""
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_WALK_SPEED
        self.x_accel = c.WALK_ACCEL
        self.y_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY
        
    def setup_counters(self):
        """These keep track of various total for important values"""
        self.frame_index = 0
        
    def load_images_from_sheet(self):
        
        self.right_frames = []
        self.left_frames = []
        
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        self.right_frames.append(
            self.get_image(5,1,41,49))
            
        for frame in self.right_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_frames.append(new_image)
            
    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        return image
        
    def update(self, keys, game_info):
        """Updates Juwico's states and animations once per frame"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state(keys)
        self.animation()
        
    def handle_state(self, keys):
        """Determines Juwicos behavior based on his state"""
        if self.state == c.STAND:
            self.standing(keys)
        elif self.state == c.WALK:
            self.walking(keys)
            
    def standing(self, keys):
        """This function is called if Juwico is standing still"""
        
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0

        if keys[tools.keybinding['down']]:
            self.facing_down = True
            self.state = c.WALK
            
        if keys[tools.keybinding['up']]:
            self.facing_down = False
            self.state = c.WALK

        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.state = c.WALK
        
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.state = c.WALK
        
        else:
            self.state = c.STAND
    def walking(self,keys):
        """test"""
        if keys[tools.keybinding['left']]:
            self.x_vel -= self.x_accel
            self.facing_right = False
        elif keys[tools.keybinding['right']]:
            self.x_vel += self.x_accel
            self.facing_right = True
        elif keys[tools.keybinding['up']]:
            self.y_vel -= self.y_accel
        elif keys[tools.keybinding['down']]:
            self.y_vel += self.y_accel
        else:
        
            
            if self.x_vel > 0:
                self.x_vel -= self.x_accel
            elif self.x_vel < 0:
                self.x_vel += self.x_accel
            else:
                self.x_vel = 0
                if self.y_vel == 0:
                    self.state = c.STAND
            
            if self.y_vel > 0:
                self.y_vel -= self.y_accel
            elif self.y_vel < 0:
                self.y_vel += self.y_accel
            else:
                self.y_vel = 0
                if self.x_vel == 0:
                    self.state = c.STAND
                    
    def calculate_animation_speed(self):
        """Used to make walking animation speed be in relation to
        Juwico's x_vel"""
        if self.x_vel == 0 :
            animation_speed_x = 130
        elif self.x_vel > 0:
            animation_speed_x = 130 - (self.x_vel * (13))
        else:
            animation_speed_x = 130 - (self.x_vel * (13) * -1)
        
        return animation_speed_x
        
    def animation(self):
        """Adjusts Juwico's image for animation"""
        if self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]
    