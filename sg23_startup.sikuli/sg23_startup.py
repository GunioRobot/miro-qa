import sys
import unittest
import time
from sikuli.Sikuli import *
import base_testcase
import myLib.config
from myLib.miro_regions import MiroRegions
from myLib.miro_app import MiroApp

class Miro_Suite(base_testcase.Miro_unittest_testcase):
    """Subgroup 1 - Install tests - going to delete preferences and database, and video storage before running each test case.

    """


    def setUp(self):
        self.verificationErrors = []
        miro = MiroApp()
        print "starting test: ",self.shortDescription()
        miro.quit_miro()
        myLib.config.set_def_db_and_prefs()
        miro.restart_miro()
        time.sleep(10)        
        
            
    def test_236(self):
        """http://litmus.pculture.org/show_test.cgi?id=236 startup, corrupt item_info_cache

        Litmus Test Title:: 236 - rebuild item_info_cache on startup.
        Description: 
        1. Clean up Miro support and vidoes directories
        2. Launch - walk through 1st tieme install dialog and search everywhere
        """

        reg = MiroRegions() 
        miro = MiroApp()
        folder_path = os.path.join(os.getenv("PCF_TEST_HOME"),"Miro","TestData")
        miro.add_watched_folder(reg, folder_path)
        miro.quit_miro()
        myLib.config.delete_preferences()
        setAutoWaitTimeout(testvars.timeout)
        #set the search regions 
        miro.restart_miro()
        miro.first_time_startup_dialog(lang="Default",run_on_start="No",search="No",search_path=None,itunes="No")    
        waitVanish("Preparing")
        time.sleep(10)
        reg = MiroRegions() 
        miro = MiroApp()
        miro.click_sidebar_tab(reg, "Videos")
        miro.tab_search(reg, title="Deerhunter",confirm_present=True)


    def test_235(self):
        """http://litmus.pculture.org/show_test.cgi?id=235 startup missing movies dir, no downloads

        Litmus Test Title:: 235 - startup missing movies dir.
        Description: 
        1. delete movies dir, launch miro
        2. 
        """
        miro.quit_miro()
        myLib.config.delete_miro_video_storage_dir()
        setAutoWaitTimeout(testvars.timeout)
        #set the search regions
        miro.restart_miro()
        reg = MiroRegions() 
        miro = MiroApp()



        
    def test_999reset(self):
        """fake test to reset db and preferences.

        """
        miro = MiroApp()
        miro.quit_miro()
        myLib.config.set_def_db_and_prefs()
        miro.restart_miro()
        time.sleep(10)
        

if __name__ == "__main__":
    import LitmusTestRunner
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv, ).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(Miro_Suite, ).litmus_test_run()


