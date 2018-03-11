import pygame as pg
from .. import setup, tools
from .. import constants as c

class Juwico(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['juwico_sheet']

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
        self.death_timer = 0
        self.transition_timer = 0
        self.flag_pole_timer = 0
        
    def setup_state_booleans(self):
        """Sets up booleans that affect Juwico's behavior"""
        self.facing_right = True
        self.allow_jump = True
        self.dead = False
        self.in_transition_state = False
        self.in_castle = False
        
    def setup_forces(self):
        """Sets up forces that affect Juwico's velocity"""
        self.x_vel = 0
        self.y_vel = 0
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY
        
    def setup_counters(self):
        """These keep track of various total for important values"""
        self.frame_index = 0
        self.flag_pole_right = 0
        
    
    def load_images_from_sheet(self):
        """Extracts Juwico's images from his sprite sheet and assigns
        them to appropriate lists"""
        
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []


        #Images for normal small juwico#

        self.right_small_normal_frames.append(
            self.get_image(104,5,12,18))  # Right [0]     #########
        self.right_small_normal_frames.append(
            self.get_image(2,6,15,18))  # Right walking 1 [1]    #########
        self.right_small_normal_frames.append(
            self.get_image(25,5,9,19))  # Right walking 2 [2]   #########
        self.right_small_normal_frames.append(
            self.get_image(44,5,12,20))  # Right walking 3 [3]   ##########
        self.right_small_normal_frames.append(
            self.get_image(60,5,19,19))  # Right jump [4]           ###########
        self.right_small_normal_frames.append(
            self.get_image(104,5,12,18))  # Right skid [5]        #############
        self.right_small_normal_frames.append(
            self.get_image(81,5,17,20))  # Death frame [6]         #############
        self.right_small_normal_frames.append(
            self.get_image(320, 8, 16, 24))  # useless
        self.right_small_normal_frames.append(
            self.get_image(241, 33, 16, 16))  # useless
        self.right_small_normal_frames.append(
            self.get_image(123,6,14,17))  # Frame 1 of flag pole Slide [9]    ###########
        self.right_small_normal_frames.append(
            self.get_image(143,6,14,17))  # Frame 2 of flag pole slide [10]   ############




        #The left image frames are numbered the same as the right
        #frames but are simply reversed.

        for frame in self.right_small_normal_frames:
            new_image = pg.transform.flip(frame, True, False)
            self.left_small_normal_frames.append(new_image)



        self.normal_small_frames = [self.right_small_normal_frames,
                              self.left_small_normal_frames]


        self.all_images = [self.right_small_normal_frames,
                           self.left_small_normal_frames]


        self.right_frames = self.normal_small_frames[0]
        self.left_frames = self.normal_small_frames[1]
    
    
    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        image.fill(c.GREEN)
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.GREEN)
        image = pg.transform.scale(image,
                                   (int(rect.width*2.7),
                                    int(rect.height*2.7)))
        return image
        
    def update(self, keys, game_info, nothing=None):
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
        elif self.state == c.JUMP:
            self.jumping(keys)
        elif self.state == c.FALL:
            self.falling(keys)
        elif self.state == c.DEATH_JUMP:
            self.jumping_to_death()
        elif self.state == c.FLAGPOLE:
            self.flag_pole_sliding()
        elif self.state == c.BOTTOM_OF_POLE:
            self.sitting_at_bottom_of_pole()
        elif self.state == c.WALKING_TO_CASTLE:
            self.walking_to_castle()
        elif self.state == c.END_OF_LEVEL_FALL:
            self.falling_at_end_of_level()
            
    def standing(self, keys):
        """This function is called if Juwico is standing still"""
        self.check_to_allow_jump(keys)
        
        self.frame_index = 0
        self.x_vel = 0
        self.y_vel = 0


        if keys[tools.keybinding['left']]:
            self.facing_right = False
            self.state = c.WALK
        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            self.state = c.WALK
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                setup.SFX['small_jump'].play()
                self.state = c.JUMP
                self.y_vel = c.JUMP_VEL
        else:
            self.state = c.STAND
        
    def check_to_allow_jump(self, keys):
        """Check to allow Juwico to jump"""
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True
        
    def walking(self, keys):
        """This function is called when Juwico is in a walking state
        It changes the frame, checks for holding down the run button,
        checks for a jump, then adjusts the state if necessary"""

        self.check_to_allow_jump(keys)

        if self.frame_index == 0:
            self.frame_index += 1
            self.walking_timer = self.current_time
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 1

                self.walking_timer = self.current_time


        self.max_x_vel = c.MAX_WALK_SPEED
        self.x_accel = c.WALK_ACCEL

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                setup.SFX['small_jump'].play()
                self.state = c.JUMP
                if self.x_vel > 4.5 or self.x_vel < -4.5:
                    self.y_vel = c.JUMP_VEL - .5
                else:
                    self.y_vel = c.JUMP_VEL


        if keys[tools.keybinding['left']]:
            self.facing_right = False
            if self.x_vel > 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel > (self.max_x_vel * -1):
                self.x_vel -= self.x_accel
                if self.x_vel > -0.5:
                    self.x_vel = -0.5
            elif self.x_vel < (self.max_x_vel * -1):
                self.x_vel += self.x_accel

        elif keys[tools.keybinding['right']]:
            self.facing_right = True
            if self.x_vel < 0:
                self.frame_index = 5
                self.x_accel = c.SMALL_TURNAROUND
            else:
                self.x_accel = c.WALK_ACCEL

            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
                if self.x_vel < 0.5:
                    self.x_vel = 0.5
            elif self.x_vel > self.max_x_vel:
                self.x_vel -= self.x_accel

        else:
            if self.facing_right:
                if self.x_vel > 0:
                    self.x_vel -= self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND
            else:
                if self.x_vel < 0:
                    self.x_vel += self.x_accel
                else:
                    self.x_vel = 0
                    self.state = c.STAND
                    
    def calculate_animation_speed(self):
        """Used to make walking animation speed be in relation to
        Juwico's x-vel"""
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed
        
    def jumping(self, keys):
        """Called when Juwico is in a JUMP state."""
        self.allow_jump = False
        self.frame_index = 4
        self.gravity = c.JUMP_GRAVITY
        self.y_vel += self.gravity

        if self.y_vel >= 0 and self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.GRAVITY
            self.state = c.FALL
                
                
    def falling(self, keys):
        """Called when Juwico is in a FALL state"""
        if self.y_vel < c.MAX_Y_VEL:
            self.y_vel += self.gravity

        if keys[tools.keybinding['left']]:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel


    def jumping_to_death(self):
        """Called when Juwico is in a DEATH_JUMP state"""
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 500:
            self.rect.y += self.y_vel
            self.y_vel += self.gravity
            
    def start_death_jump(self, game_info):
        """Used to put Juwico in a DEATH_JUMP state"""
        self.dead = True
        game_info[c.JUWICO_DEAD] = True
        self.y_vel = -11
        self.gravity = .5
        self.frame_index = 6
        self.image = self.right_frames[self.frame_index]
        self.state = c.DEATH_JUMP
        self.in_transition_state = True
    
    def flag_pole_sliding(self):
        """State where Juwico is sliding down the flag pole"""
        self.state = c.FLAGPOLE
        self.in_transition_state = True
        self.x_vel = 0
        self.y_vel = 0

        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
        elif self.rect.bottom < 420:
            if (self.current_time - self.flag_pole_timer) < 65:
                self.image = self.right_frames[9]
            elif (self.current_time - self.flag_pole_timer) < 130:
                self.image = self.right_frames[10]
            elif (self.current_time - self.flag_pole_timer) >= 130:
                self.flag_pole_timer = self.current_time

            self.rect.right = self.flag_pole_right
            self.y_vel = 5
            self.rect.y += self.y_vel

            if self.rect.bottom >= 415:
                self.flag_pole_timer = self.current_time

        elif self.rect.bottom >= 420:
            self.image = self.right_frames[10]
            
    def sitting_at_bottom_of_pole(self):
        """State when juwico is at the bottom of the flag pole"""
        if self.flag_pole_timer == 0:
            self.flag_pole_timer = self.current_time
            self.image = self.left_frames[10]
        elif (self.current_time - self.flag_pole_timer) < 210:
            self.image = self.left_frames[10]
        else:
            self.in_transition_state = False
            if self.rect.bottom < 485:
                self.state = c.END_OF_LEVEL_FALL
            else:
                self.state = c.WALKING_TO_CASTLE


    def set_state_to_bottom_of_pole(self):
        """Sets Juwico to the BOTTOM_OF_POLE state"""
        self.image = self.left_frames[9]
        right = self.rect.right
        self.rect.bottom = c.GROUND_HEIGHT
        self.rect.x = right
        self.flag_pole_timer = 0
        self.state = c.BOTTOM_OF_POLE
        
    def walking_to_castle(self):
        """State when Juwico walks to the castle to end the level"""
        self.max_x_vel = 5
        self.x_accel = c.WALK_ACCEL

        if self.x_vel < self.max_x_vel:
            self.x_vel += self.x_accel

        if (self.walking_timer == 0 or (self.current_time - self.walking_timer) > 200):
            self.walking_timer = self.current_time

        elif (self.current_time - self.walking_timer) > \
                self.calculate_animation_speed():
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 1
            self.walking_timer = self.current_time


    def falling_at_end_of_level(self, *args):
        """State when Juwico is falling from the flag pole base"""
        self.y_vel += c.GRAVITY

    
    def animation(self):
        """Adjusts Juwico's image for animation"""
        if self.state == c.DEATH_JUMP \
            or self.state == c.FLAGPOLE \
            or self.state == c.BOTTOM_OF_POLE:
            pass
        elif self.facing_right:
            self.image = self.right_frames[self.frame_index]
        else:
            self.image = self.left_frames[self.frame_index]