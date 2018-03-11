from . import setup,tools
from .states import main_menu,load_screen,level1,intro,level2,level3,level4,level0,one_frame
from . import constants as c

def main():
    """Add states to control here."""
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LOAD_SCREEN1: load_screen.LoadScreenBack(1),
                  c.LOAD_SCREEN2: load_screen.LoadScreenBack(2),
                  c.LOAD_SCREEN3: load_screen.LoadScreenBack(3),
                  c.LOAD_SCREEN4: load_screen.LoadScreenBack(4),
                  c.INTRO: intro.Intro(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1(),
                  c.LEVEL2: level2.Level2(),
                  c.LEVEL3: level3.Level3(),
                  c.LEVEL4: level4.Level4(),
                  c.LEVEL0 : level0.Level0(),
                  c.HELP : one_frame.Help(),
                  c.END1 : one_frame.End1(),
                  c.END2 : one_frame.End2(),
                  c.END3 : one_frame.End3(),
                  c.END4 : one_frame.End4(),
                  c.END5 : one_frame.End5()}

    run_it.setup_states(state_dict, c.MAIN_MENU)
    run_it.main()