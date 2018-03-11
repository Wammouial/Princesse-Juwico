import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. import game_sound
from .. classes import juwico
from .. classes import collider
from .. classes import enemies
from .. classes import checkpoint
from .. classes import flagpole
from .. classes import info
from .. classes import score
from .. classes import castle_flag


class Level4(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        """Called when the State object is created"""
        self.game_info = persist
        self.persist = self.game_info
        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.LEVEL_STATE] = c.NOT_FROZEN
        self.game_info[c.JUWICO_DEAD] = False
        self.game_info[c.COIN_TOTAL] = 1
        self.game_info[c.LEVEL_NUMBER] = '1-4'

        self.state = c.NOT_FROZEN
        self.death_timer = 0
        self.flag_timer = 0
        self.flag_score = None
        self.flag_score_total = 0

        self.moving_score_list = []
        self.overhead_info_display = info.OverheadInfo(self.game_info, c.LEVEL4)
        self.sound_manager = game_sound.Sound(self.overhead_info_display)
        self.powerup_group = []

        self.setup_background()
        self.setup_steps()
        self.setup_flag_pole()
        self.setup_enemies()
        self.setup_juwico()
        self.setup_checkpoints()
        self.setup_spritegroups()
        
    def setup_background(self):
        """Sets the background image, rect and scales it to the correct
        proportions"""
        self.background = setup.GFX['level_4']
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                  (int(self.back_rect.width*c.BACKGROUND_MULTIPLER),
                                  int(self.back_rect.height*c.BACKGROUND_MULTIPLER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width, height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game_info[c.CAMERA_START_X]
                                          
    def setup_steps(self):
        """Create collideable rects for all the steps"""
        step1 = collider.Collider(36,424,159,88)
        step2 = collider.Collider(272,311,159,88)
        
        step3 = collider.Collider(425,419,159,88)
        step4 = collider.Collider(637,424,160,88)


        step5 = collider.Collider(833,263,159,82)
        step6 = collider.Collider(1350,452,158,87)
        
        step7 = collider.Collider(1581,248,159,84)
        step8 = collider.Collider(1895,303,156,88)

        step9 = collider.Collider(2217,316,158,88)
        step10 = collider.Collider(2636,488,160,87)
        
        step11 = collider.Collider(2816,316,159,88)
        step12 = collider.Collider(3112,236,160,88)
        
        step13 = collider.Collider(3236,488,160,87)
        step14 = collider.Collider(3416,316,160,88)
        
        step15 = collider.Collider(3848,316,160,88)
        step16 = collider.Collider(4236,424,160,88)
        step17 = collider.Collider(4414,465,386,135)
        
        step18 = collider.Collider(1490,357,160,89)
        step19 = collider.Collider(2483,348,160,88)

        self.step_group = pg.sprite.Group(step1,  step2,
                                          step3,  step4,
                                          step5,  step6,
                                          step7,  step8,
                                          step9,  step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19)
    def setup_flag_pole(self):
        """Creates the flag pole at the end of the level"""
        self.flag = flagpole.Flag(4600, 100)

        pole0 = flagpole.Pole(4600, 97)
        pole1 = flagpole.Pole(4600, 137)
        pole2 = flagpole.Pole(4600, 177)
        pole3 = flagpole.Pole(4600, 217)
        pole4 = flagpole.Pole(4600, 257)
        pole5 = flagpole.Pole(4600, 297)
        pole6 = flagpole.Pole(4600, 337)
        pole7 = flagpole.Pole(4600, 377)
        pole8 = flagpole.Pole(4600, 417)
        pole9 = flagpole.Pole(4600, 437)

        finial = flagpole.Finial(4600, 97)

        self.flag_pole_group = pg.sprite.Group(self.flag,
                                               finial,
                                               pole0,
                                               pole1,
                                               pole2,
                                               pole3,
                                               pole4,
                                               pole5,
                                               pole6,
                                               pole7,
                                               pole8,
                                               pole9)
    
    
    def setup_enemies(self):   
        """Creates all the enemies and stores them in a list of lists."""
        laideron0 = enemies.Laideron()
        laideron1 = enemies.Laideron()
        laideron2 = enemies.Laideron()
        laideron3 = enemies.Laideron()
        laideron4 = enemies.Laideron()
        laideron5 = enemies.Laideron()
        laideron6 = enemies.Laideron()
        laideron7 = enemies.Laideron()
        laideron8 = enemies.Laideron()
        laideron9 = enemies.Laideron()
        laideron10 = enemies.Laideron()
        laideron11 = enemies.Laideron()
        laideron12 = enemies.Laideron()
        laideron13 = enemies.Laideron()
        laideron14 = enemies.Laideron()
        laideron15 = enemies.Laideron()

        enemy_group1 = pg.sprite.Group(laideron0)
        enemy_group2 = pg.sprite.Group(laideron1)
        enemy_group3 = pg.sprite.Group(laideron2, laideron3)
        enemy_group4 = pg.sprite.Group(laideron4, laideron5)
        enemy_group5 = pg.sprite.Group(laideron6, laideron7)

        self.enemy_group_list = [enemy_group1,
                                 enemy_group2,
                                 enemy_group3,
                                 enemy_group4,
                                 enemy_group5]
                                 
    def setup_juwico(self):
        """Places Juwico at the beginning of the level"""
        self.juwico = juwico.Juwico()
        self.juwico.rect.x =  50
        self.juwico.rect.bottom = c.GROUND_HEIGHT_LEVEL4
    
    def setup_checkpoints(self):
        """Creates invisible checkpoints that when collided will trigger
        the creation of enemies from the self.enemy_group_list"""
        check1 = checkpoint.Checkpoint(700, "1")
        check2 = checkpoint.Checkpoint(1077, '2')
        check3 = checkpoint.Checkpoint(1674, '3')
        check4 = checkpoint.Checkpoint(3080, '4')  
        check5 = checkpoint.Checkpoint(3785, '5')
        check6 = checkpoint.Checkpoint(4150, '6')
        check7 = checkpoint.Checkpoint(4470, '7')
        check8 = checkpoint.Checkpoint(4950, '8')
        check9 = checkpoint.Checkpoint(5100, '9')
        check10 = checkpoint.Checkpoint(6800, '10')
        check11 = checkpoint.Checkpoint(4600, '11', 5, 6)
        check12 = checkpoint.Checkpoint(4600+200, '12')
        check13 = checkpoint.Checkpoint(2740, 'secret_mushroom', 360, 40, 12)

        self.check_point_group = pg.sprite.Group(check1, check2, check3,
                                                 check4, check5, check6,
                                                 check7, check8, check9,
                                                 check10, check11, check12,
                                                 check13)
    #A voir                                      
    def setup_spritegroups(self):
        """Sprite groups created for convenience"""
        self.sprites_about_to_die_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.ground_step_pipe_group = pg.sprite.Group(self.step_group)
                                                      

        self.juwico_and_enemy_group = pg.sprite.Group(self.juwico,
                                                      self.enemy_group)
                                                     
    
    def update(self, surface, keys, current_time):
        """Updates Entire level using states.  Called by the control object"""
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.handle_states(keys)
        self.check_if_time_out()
        self.blit_everything(surface)
        self.sound_manager.update(self.game_info, self.juwico)
        
    def handle_states(self, keys):
        """If the level is in a FROZEN state, only juwico will update"""
        if self.state == c.FROZEN:
            self.update_during_transition_state(keys)
        elif self.state == c.NOT_FROZEN:
            self.update_all_sprites(keys)
        elif self.state == c.IN_CASTLE:
            self.update_while_in_castle()
        elif self.state == c.FLAG_AND_FIREWORKS:
            self.update_flag_and_fireworks()
            
    def update_during_transition_state(self, keys):
        """Updates juwico in a transition state (like becoming big, small,
         or dies). Checks if he leaves the transition state or dies to
         change the level state back"""
        self.juwico.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.flag_pole_group.update(self.game_info)
        self.check_if_juwico_in_transition_state()
        self.check_flag()
        self.check_for_juwico_death()
        self.overhead_info_display.update(self.game_info, self.juwico)
        
    def check_if_juwico_in_transition_state(self):
        """If juwico is in a transition state, the level will be in a FREEZE
        state"""
        if self.juwico.in_transition_state:
            self.game_info[c.LEVEL_STATE] = self.state = c.FROZEN
        elif self.juwico.in_transition_state == False:
            if self.state == c.FROZEN:
                self.game_info[c.LEVEL_STATE] = self.state = c.NOT_FROZEN
                
    def update_all_sprites(self, keys):
        """Updates the location of all sprites on the screen."""
        self.juwico.update(keys, self.game_info, self.powerup_group)
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        if self.flag_score:
            self.flag_score.update(None, self.game_info)
            self.check_to_add_flag_score()
        self.flag_pole_group.update()
        #PAs pour moment
        self.check_points_check()
        self.enemy_group.update(self.game_info)
        self.sprites_about_to_die_group.update(self.game_info, self.viewport)
        self.adjust_sprite_positions()
        self.check_if_juwico_in_transition_state()
        self.check_for_juwico_death()
        self.update_viewport()
        self.overhead_info_display.update(self.game_info, self.juwico)
    
    
    def check_points_check(self):
        """Detect if checkpoint collision occurs, delete checkpoint,
        add enemies to self.enemy_group"""
        checkpoint = pg.sprite.spritecollideany(self.juwico,
                                                 self.check_point_group)
        if checkpoint:
            checkpoint.kill()

            for i in range(1,6):
                if checkpoint.name == str(i):
                    for index, enemy in enumerate(self.enemy_group_list[i -1]):
                        enemy.rect.x = self.viewport.right + (index * 60)
                    self.enemy_group.add(self.enemy_group_list[i-1])

            if checkpoint.name == '11':
                self.juwico.state = c.FLAGPOLE
                self.juwico.invincible = False
                self.juwico.flag_pole_right = checkpoint.rect.right
                if self.juwico.rect.bottom < self.flag.rect.y:
                    self.juwico.rect.bottom = self.flag.rect.y
                self.flag.state = c.SLIDE_DOWN
                self.create_flag_points()

            elif checkpoint.name == '12':
                self.state = c.IN_CASTLE
                self.juwico.kill()
                self.juwico.state == c.STAND
                self.juwico.in_castle = True
                self.overhead_info_display.state = c.FAST_COUNT_DOWN
    
    
    def create_flag_points(self):
        """Creates the points that appear when Juwico touches the
        flag pole"""
        x = 4600
        y = c.GROUND_HEIGHT
        juwico_bottom = self.juwico.rect.bottom

        if juwico_bottom > (c.GROUND_HEIGHT - 40 - 40):
            self.flag_score = score.Score(x, y, 100, True)
            self.flag_score_total = 100
        elif juwico_bottom > (c.GROUND_HEIGHT - 40 - 160):
            self.flag_score = score.Score(x, y, 400, True)
            self.flag_score_total = 400
        elif juwico_bottom > (c.GROUND_HEIGHT - 40 - 240):
            self.flag_score = score.Score(x, y, 800, True)
            self.flag_score_total = 800
        elif juwico_bottom > (c.GROUND_HEIGHT - 40 - 360):
            self.flag_score = score.Score(x, y, 2000, True)
            self.flag_score_total = 2000
        else:
            self.flag_score = score.Score(x, y, 5000, True)
            self.flag_score_total = 5000

    def adjust_sprite_positions(self):
        """Adjusts sprites by their x and y velocities and collisions"""
        self.adjust_juwico_position()
        self.adjust_enemy_position()
        
    def adjust_juwico_position(self):
        """Adjusts Juwico's position based on his x, y velocities and
        potential collisions"""
        self.last_x_position = self.juwico.rect.right
        self.juwico.rect.x += round(self.juwico.x_vel)
        self.check_juwico_x_collisions()

        if self.juwico.in_transition_state == False:
            self.juwico.rect.y += round(self.juwico.y_vel)
            self.check_juwico_y_collisions()

        if self.juwico.rect.x < (self.viewport.x + 5):
            self.juwico.rect.x = (self.viewport.x + 5)
    
        
    def check_juwico_x_collisions(self):
        """Check for collisions after Juwico is moved on the x axis"""
        collider = pg.sprite.spritecollideany(self.juwico, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(self.juwico, self.enemy_group)

        if collider:
            self.adjust_juwico_for_x_collisions(collider)

        elif enemy:
            self.juwico.start_death_jump(self.game_info)
            self.state = c.FROZEN

    
    def adjust_juwico_for_x_collisions(self, collider):
        """Puts Juwico flush next to the collider after moving on the x axis"""
        if self.juwico.rect.x < collider.rect.x:
            self.juwico.rect.right = collider.rect.left
        else:
            self.juwico.rect.left = collider.rect.right

        self.juwico.x_vel = 0
                    
    def check_juwico_y_collisions(self):
        """Checks for collisions when Juwico moves along the y-axis"""
        ground_step_or_pipe = pg.sprite.spritecollideany(self.juwico, self.ground_step_pipe_group)
        enemy = pg.sprite.spritecollideany(self.juwico, self.enemy_group)

        if ground_step_or_pipe:
            self.adjust_juwico_for_y_ground_pipe_collisions(ground_step_or_pipe)

        elif enemy:
            self.adjust_juwico_for_y_enemy_collisions(enemy)

        self.test_if_juwico_is_falling()


    def adjust_juwico_for_y_ground_pipe_collisions(self, collider):
        """Juwico collisions with pipes on the y-axis"""
        if collider.rect.bottom > self.juwico.rect.bottom:
            self.juwico.y_vel = 0
            self.juwico.rect.bottom = collider.rect.top
            if self.juwico.state == c.END_OF_LEVEL_FALL:
                self.juwico.state = c.WALKING_TO_CASTLE
            else:
                self.juwico.state = c.WALK
        elif collider.rect.top < self.juwico.rect.top:
            self.juwico.y_vel = 7
            self.juwico.rect.top = collider.rect.bottom
            self.juwico.state = c.FALL
            
    def test_if_juwico_is_falling(self):
        """Changes Juwico to a FALL state if more than a pixel above a pipe,
        ground, step or box"""
        self.juwico.rect.y += 1
        test_collide_group = pg.sprite.Group(self.ground_step_pipe_group)


        if pg.sprite.spritecollideany(self.juwico, test_collide_group) is None:
            if self.juwico.state != c.JUMP \
                and self.juwico.state != c.DEATH_JUMP \
                and self.juwico.state != c.SMALL_TO_BIG \
                and self.juwico.state != c.BIG_TO_FIRE \
                and self.juwico.state != c.BIG_TO_SMALL \
                and self.juwico.state != c.FLAGPOLE \
                and self.juwico.state != c.WALKING_TO_CASTLE \
                and self.juwico.state != c.END_OF_LEVEL_FALL:
                self.juwico.state = c.FALL
            elif self.juwico.state == c.WALKING_TO_CASTLE or \
                self.juwico.state == c.END_OF_LEVEL_FALL:
                self.juwico.state = c.END_OF_LEVEL_FALL

        self.juwico.rect.y -= 1
    
    def adjust_juwico_for_y_enemy_collisions(self, enemy):
        """Juwico collisions with all enemies on the y-axis"""
        if self.juwico.y_vel > 0:
            setup.SFX['stomp'].play()
            self.game_info[c.SCORE] += 100
            self.moving_score_list.append(
                score.Score(enemy.rect.centerx - self.viewport.x,
                            enemy.rect.y, 100))
            enemy.state = c.JUMPED_ON
            enemy.kill()
            if enemy.name == c.LAIDERON:
                enemy.death_timer = self.current_time
                self.sprites_about_to_die_group.add(enemy)

            self.juwico.rect.bottom = enemy.rect.top
            self.juwico.state = c.JUMP
            self.juwico.y_vel = -7

                
    def adjust_enemy_position(self):
        """Moves all enemies along the x, y axes and check for collisions"""
        for enemy in self.enemy_group:
            enemy.rect.x += enemy.x_vel
            self.check_enemy_x_collisions(enemy)

            enemy.rect.y += enemy.y_vel
            self.check_enemy_y_collisions(enemy)
            self.delete_if_off_screen(enemy)


    def check_enemy_x_collisions(self, enemy):
        """Enemy collisions along the x axis.  Removes enemy from enemy group
        in order to check against all other enemies then adds it back."""
        enemy.kill()

        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)
        enemy_collider = pg.sprite.spritecollideany(enemy, self.enemy_group)

        if collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = collider.rect.left
                enemy.direction = c.LEFT
                enemy.x_vel = -2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = collider.rect.right
                enemy.direction = c.RIGHT
                enemy.x_vel = 2


        elif enemy_collider:
            if enemy.direction == c.RIGHT:
                enemy.rect.right = enemy_collider.rect.left
                enemy.direction = c.LEFT
                enemy_collider.direction = c.RIGHT
                enemy.x_vel = -2
                enemy_collider.x_vel = 2
            elif enemy.direction == c.LEFT:
                enemy.rect.left = enemy_collider.rect.right
                enemy.direction = c.RIGHT
                enemy_collider.direction = c.LEFT
                enemy.x_vel = 2
                enemy_collider.x_vel = -2

        self.enemy_group.add(enemy)
        self.juwico_and_enemy_group.add(self.enemy_group)
        
    def check_enemy_y_collisions(self, enemy):
        """Enemy collisions on the y axis"""
        collider = pg.sprite.spritecollideany(enemy, self.ground_step_pipe_group)

        if collider:
            if enemy.rect.bottom > collider.rect.bottom:
                enemy.y_vel = 7
                enemy.rect.top = collider.rect.bottom
                enemy.state = c.FALL
            elif enemy.rect.bottom < collider.rect.bottom:

                enemy.y_vel = 0
                enemy.rect.bottom = collider.rect.top
                enemy.state = c.WALK

        else:
            enemy.rect.y += 1
            test_group = pg.sprite.Group(self.ground_step_pipe_group)
            if pg.sprite.spritecollideany(enemy, test_group) is None:
                if enemy.state != c.JUMP:
                    enemy.state = c.FALL

            enemy.rect.y -= 1

    def check_if_falling(self, sprite, sprite_group):
        """Checks if sprite should enter a falling state"""
        sprite.rect.y += 1

        if pg.sprite.spritecollideany(sprite, sprite_group) is None:
            if sprite.state != c.JUMP:
                sprite.state = c.FALL

        sprite.rect.y -= 1


    def delete_if_off_screen(self, enemy):
        """Removes enemy from sprite groups if 500 pixels left off the screen,
         underneath the bottom of the screen, or right of the screen if shell"""
        if enemy.rect.x < (self.viewport.x - 300):
            enemy.kill()

        elif enemy.rect.y > (self.viewport.bottom):
            enemy.kill()

        elif enemy.state == c.SHELL_SLIDE:
            if enemy.rect.x > (self.viewport.right + 500):
                enemy.kill()
                
    def check_flag(self):
        """Adjusts juwico's state when the flag is at the bottom"""
        if (self.flag.state == c.BOTTOM_OF_POLE
            and self.juwico.state == c.FLAGPOLE):
            self.juwico.set_state_to_bottom_of_pole()


    def check_to_add_flag_score(self):
        """Adds flag score if at top"""
        if self.flag_score.y_vel == 0:
            self.game_info[c.SCORE] += self.flag_score_total
            self.flag_score_total = 0


    def check_for_juwico_death(self):
        """Restarts the level if Juwico is dead"""
        if self.juwico.rect.y > c.SCREEN_HEIGHT and not self.juwico.in_castle:
            self.juwico.dead = True
            self.juwico.x_vel = 0
            self.state = c.FROZEN
            self.game_info[c.JUWICO_DEAD] = True

        if self.juwico.dead:
            self.play_death_song()


    def play_death_song(self):
        if self.death_timer == 0:
            self.death_timer = self.current_time
        elif (self.current_time - self.death_timer) > 3000:
            self.set_game_info_values()
            self.done = True


    def set_game_info_values(self):
        """sets the new game values after a player's death"""
        if self.game_info[c.SCORE] > self.persist[c.TOP_SCORE]:
            self.persist[c.TOP_SCORE] = self.game_info[c.SCORE]
        if self.juwico.dead:
            self.persist[c.LIVES] -= 1

        if self.persist[c.LIVES] == 0:
            self.next = c.GAME_OVER
            self.game_info[c.CAMERA_START_X] = 0
        elif self.juwico.dead == False:
            self.next = c.MAIN_MENU
            self.game_info[c.CAMERA_START_X] = 0
        elif self.overhead_info_display.time == 0:
            self.next = c.TIME_OUT
        else:
            if self.juwico.rect.x > 3670 \
                    and self.game_info[c.CAMERA_START_X] == 0:
                self.game_info[c.CAMERA_START_X] = 0
            self.next = c.LOAD_SCREEN4
            
    def check_if_time_out(self):
        """Check if time has run down to 0"""
        if self.overhead_info_display.time <= 0 \
                and not self.juwico.dead \
                and not self.juwico.in_castle:
            self.state = c.FROZEN
            self.juwico.start_death_jump(self.game_info)


    def update_viewport(self):
        """Changes the view of the camera"""
        third = self.viewport.x + self.viewport.w//3
        juwico_center = self.juwico.rect.centerx
        juwico_right = self.juwico.rect.right

        if self.juwico.x_vel > 0 and juwico_center >= third:
            mult = 0.5 if juwico_right < self.viewport.centerx else 1
            new = self.viewport.x + mult * self.juwico.x_vel
            highest = self.level_rect.w - self.viewport.w
            self.viewport.x = min(highest, new)
            
    def update_while_in_castle(self):
        """Updates while Juwico is in castle at the end of the level"""
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)

        if self.overhead_info_display.state == c.END_OF_LEVEL:
            self.state = c.FLAG_AND_FIREWORKS
            self.flag_pole_group.add(castle_flag.Flag(4600+120, 322))


    def update_flag_and_fireworks(self):
        """Updates the level for the fireworks and castle flag"""
        for score in self.moving_score_list:
            score.update(self.moving_score_list, self.game_info)
        self.overhead_info_display.update(self.game_info)
        self.flag_pole_group.update()

        self.end_game()
        
    def end_game(self):
        """End the game"""
        if self.flag_timer == 0:
            self.flag_timer = self.current_time
        elif (self.current_time - self.flag_timer) > 2000:
            self.set_game_info_values()
            self.game_info[c.COIN_TOTAL] = 0
            self.next = c.END4
            self.sound_manager.stop_music()
            self.done = True


    def blit_everything(self, surface):
        """Blit all sprites to the main surface"""
        self.level.blit(self.background, self.viewport, self.viewport)
        if self.flag_score:
            self.flag_score.draw(self.level)
        #self.step_group.draw(self.level)
        self.sprites_about_to_die_group.draw(self.level)
        #self.check_point_group.draw(self.level)   #If needed
        self.flag_pole_group.draw(self.level)
        self.juwico_and_enemy_group.draw(self.level)

        surface.blit(self.level, (0,0), self.viewport)
        self.overhead_info_display.draw(surface)
        for score in self.moving_score_list:
            score.draw(surface)
