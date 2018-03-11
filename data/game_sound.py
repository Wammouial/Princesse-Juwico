import pygame as pg
from . import setup
from . import constants as c


class Sound(object):
    """Handles all sound for the game"""
    def __init__(self, overhead_info):
        """Initialize the class"""
        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()


    def set_music_mixer(self):
            """Sets music for level"""
            if self.overhead_info.state == c.LEVEL1:
                pg.mixer.music.load(self.music_dict['level1'])
                pg.mixer.music.play()
                self.state = c.NORMAL
            elif self.overhead_info.state == c.LEVEL2:
                pg.mixer.music.load(self.music_dict['level2'])
                pg.mixer.music.play()
                self.state = c.NORMAL
            elif self.overhead_info.state == c.LEVEL3:
                pg.mixer.music.load(self.music_dict['level3'])
                pg.mixer.music.play()
                self.state = c.NORMAL
            elif self.overhead_info.state == c.LEVEL4:
                pg.mixer.music.load(self.music_dict['level4'])
                pg.mixer.music.play()
                self.state = c.NORMAL
            elif self.overhead_info.state == c.LEVEL0:
                pg.mixer.music.load(self.music_dict['level0.2'])
                pg.mixer.music.play()
                self.state = c.NORMAL
            elif self.overhead_info.state == c.GAME_OVER:
                pg.mixer.music.load(self.music_dict['game_over'])
                pg.mixer.music.play()
                self.state = c.GAME_OVER
            elif self.overhead_info.state == c.INTRO:
                pg.mixer.music.load(self.music_dict['intro'])
                pg.mixer.music.play()
                
    def update(self, game_info, juwico):
        """Updates sound object with game info"""
        self.game_info = game_info
        self.juwico = juwico
        self.handle_state()
        
    def  handle_state(self):
        """Handles the state of the soundn object"""
        if self.state == c.NORMAL:
            if self.juwico.dead:
                self.play_music('death', c.JUWICO_DEAD)
            elif self.juwico.state == c.FLAGPOLE:
                self.play_music('flagpole', c.FLAGPOLE)
            elif self.overhead_info.time == 100:
                self.play_music('out_of_time', c.TIME_WARNING)


        elif self.state == c.FLAGPOLE:
            if self.juwico.state == c.WALKING_TO_CASTLE:
                self.play_music('stage_clear', c.STAGE_CLEAR)

        elif self.state == c.STAGE_CLEAR:
            if self.juwico.in_castle:
                self.sfx_dict['count_down'].play()
                self.state = c.FAST_COUNT_DOWN

        elif self.state == c.FAST_COUNT_DOWN:
            if self.overhead_info.time == 0:
                self.sfx_dict['count_down'].stop()
                self.state = c.WORLD_CLEAR

        elif self.state == c. TIME_WARNING:
            if pg.mixer.music.get_busy() == 0:
                self.play_music('main_theme_sped_up', c.SPED_UP_NORMAL)
            elif self.juwico.dead:
                self.play_music('death', c.JUWICO_DEAD)

        elif self.state == c.SPED_UP_NORMAL:
            if self.juwico.dead:
                self.play_music('death', c.JUWICO_DEAD)
            elif self.juwico.state == c.FLAGPOLE:
                self.play_music('flagpole', c.FLAGPOLE)

        elif self.state == c.WORLD_CLEAR:
            pass
        elif self.state == c.JUWICO_DEAD:
            pass
        elif self.state == c.GAME_OVER:
            pass
            
    def play_music(self, key, state):
        """Plays new music"""
        pg.mixer.music.load(self.music_dict[key])
        pg.mixer.music.play()
        self.state = state

    def stop_music(self):
        """Stops playback"""
        pg.mixer.music.stop()
