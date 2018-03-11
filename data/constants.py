SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Princesse Juwico"

## COLORS ##

#            R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

#A voir
SIZE_MULTIPLIER = 2.5
SIZE_MULTIPLIER_LAIDERON = 1.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 1
GROUND_HEIGHT = SCREEN_HEIGHT - 180
GROUND_HEIGHT_LEVEL1 = 415
GROUND_HEIGHT_LEVEL2 = 421
GROUND_HEIGHT_LEVEL3 = 532
GROUND_HEIGHT_LEVEL4 = 422

#Juwico FORCES
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6

#Juwico States

STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'


LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'


SHELL_SLIDE = 'shell slide'


RESTING = 'resting'
BUMPED = 'bumped'

OPENED = 'opened'


REVEAL = 'reveal'
SLIDE = 'slide'


SPIN = 'spin'


BOUNCE = 'bounce'


FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'


MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'


LAIDERON = 'laideron'
KOOPA = 'koopa'

ONEUP = '379'

#MAIN MENU CURSOR STATES
PLAYER1 = '1 player'
PLAYER2 = 'nothing'

#LEVEL STATES

FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#FLAG STATE
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#MAIN MENU CURSOR STATES
PLAYER1 = '1 player'


#OVERHEAD INFO STATES
MAIN_MENU = 'main menu'
LOAD_SCREEN1 = 'loading screen1'
LOAD_SCREEN2 = 'loading screen2'
LOAD_SCREEN3 = 'loading screen3'
LOAD_SCREEN4 = 'loading screen4'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'


#GAME INFO DICTIONARY KEYS
COIN_TOTAL = 'coin total'
LEVEL_NUMBER = 'level_number'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
JUWICO_DEAD = 'juwico dead'

#STATES FOR ENTIRE GAME
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL0 = 'level0'
LEVEL1 = 'level1'
LEVEL2 = 'level2'
LEVEL3 = 'level3'
LEVEL4 = 'level4'
INTRO = 'intro'
HELP = 'help'
END1 = 'end1'
END2 = 'end2'
END3 = 'end3'
END4 = 'end4'
END5 = 'end5'

#SOUND STATEZ
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'