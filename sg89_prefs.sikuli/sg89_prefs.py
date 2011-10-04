import sys
import unittest
import time
from sikuli.Sikuli import *
import base_testcase
import myLib.config
from myLib.miro_regions import MiroRegions
from myLib.miro_app import MiroApp
from myLib.pref_general_tab import PrefGeneralTab

class Miro_Suite(base_testcase.Miro_unittest_testcase):
    """Subgroup 89 - preferences tests.

    """    

    def test_1(self):
        """http://litmus.pculture.org/show_test.cgi?id=467 change sys language.

        1. Open Preferences
        2. Change the system default language
        3. Restart Miro
        4. Verify changes and reset
        5. Restart Miro
        
        """
        reg = MiroRegions()
        miro = MiroApp(reg)
        #1. open preferences
        miro.open_prefs(reg)
        prefs = PrefGeneralTab()
        prefs.change_default_language( "Croatian")
        miro.restart()
        
        miro.open_prefs(reg, menu="Datoteka", option="Postavke")
        prefs = PrefGeneralTab()
        prefs.change_to_english_language(from_lang="Croatian")
        prefs.close_prefs()
        

        
        #2. change language to croatian (hr)
##        if p.exists("System default") or p.exists("English"):
##            click(p.getLastMatch())
##        for x in range(0,3):
##            if not exists("Croatian",3):
##                type(Key.PAGE_DOWN)
##        for x in range(0,6):
##            if not exists("Croatian",3):
##                type(Key.PAGE_UP)
##        click("Croatian")
##        time.sleep(2)
##        type(Key.TAB)
##        type(Key.TAB)
##        type(Key.ENTER)
##        #miro.shortcut("w")
##        type(Key.ESC)
##        #3. Restart Miro
##        miro.quit_miro(reg)
##        miro.restart_miro()
##
##        #4. Verify Changes and reset
##        prefs.open_prefs(reg, lang='hr',menu='Datoteka',option='Postavke')
##        if p.exists("Croatian"):
##            click(p.getLastMatch())
##        else:
##            find("Jezik")
##            click(getLastMatch().right(40))
##        type(Key.PAGE_UP)
##        for x in range(0,3):
##            if exists("English",3):
##                break
##            else:
##                type(Key.PAGE_UP)
##        click("English")
##        time.sleep(2)
##        type(Key.TAB)
##        type(Key.TAB)
##        type(Key.ENTER)
##        type(Key.ESC)
##        time.sleep(2)
##        #5. Restart Miro
##        if reg.s.exists("icon-search.png",3) or \
##           reg.s.exists("icon-video.png",3):
##            click(reg.s.getLastMatch())
##            time.sleep(3)
##        miro.shortcut('q')
##        while reg.m.exists("dialog_confirm_quit.png",5):
##            reg.m.click("dialog_quit.png")
##        time.sleep(2)
##        miro.restart_miro()
##        self.assertTrue(exists("File"))
##
##    def test_999reset(self):
##        """fake test to reset db and preferences.
##
##        """
##        miro.quit_miro()
##        myLib.config.set_def_db_and_prefs()
##        miro.restart_miro()
##        time.sleep(10) 


   
# Post the output directly to Litmus
if __name__ == "__main__":
    import LitmusTestRunner
    print len(sys.argv)
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv, ).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(Miro_Suite, ).litmus_test_run()
 

