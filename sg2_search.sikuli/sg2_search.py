import sys
import os
import glob
import unittest
import StringIO
import time
from sikuli.Sikuli import *

mycwd = os.path.join(os.getenv("PCF_TEST_HOME"),"Miro")
sys.path.append(os.path.join(mycwd,'myLib'))
import config
import base_testcase
import mirolib
import testvars

class Miro_Suite(base_testcase.Miro_unittest_testcase):
    """Subgroup 2 - one-click subscribe tests.

    """             
    def test_82(self):
        """http://litmus.pculture.org/show_test.cgi?id=82 remember last search.

        1. Perform a search
        2. Click off the tab
        3. Click back and verify the search is remembered.
        4. Cleanup
        """
       
        setAutoWaitTimeout(60)
        reg = mirolib._AppRegions()

        SEARCHES = {"blip": 'octopus', "YouTube": 'cosmicomics'}
        for engine, term in SEARCHES.iteritems():
            mirolib.click_sidebar_tab(self,reg,"Search")
            mirolib.search_tab_search(self,reg,term,engine)
            mirolib.click_sidebar_tab(self,reg,"Videos")
            mirolib.click_sidebar_tab(self,reg,"Search")
            self.assertTrue(reg.mtb.exists(term.upper()))


        
    def test_322(self):
        """http://litmus.pculture.org/show_test.cgi?id=322 search and save as a podcast

        1. Perform a search
        2. Click off the tab
        3. Click back and verify the search is remembered.
        4. Cleanup
        """
        setAutoWaitTimeout(60)
        reg = mirolib._AppRegions()

        searches = {"blip": "python", "YouTube": "cosmicomics", "Revver": "beiber", "Yahoo": "Canada", "DailyMotion": "Russia", "Metavid": "africa", "Mininova": "vancouver", "Video": "toronto"}
        for engine, term in searches.iteritems():
            mirolib.click_sidebar_tab(self,reg,"search")
            mirolib.toggle_normal(reg)
            mirolib.toggle_list(reg)
            mirolib.search_tab_search(self,reg,term,engine)
            reg.mtb.click("button_save_as_podcast.png")
            if engine == "blip":
                saved_search = engine
            else:
                saved_search = engine +" for"
            mirolib.click_podcast(self,reg,saved_search)
            mirolib.shortcut("r")
            mirolib.get_podcasts_region(reg)
        for x in searches.keys():
            mirolib.tab_search(self,reg,x,confirm_present=True)
                
                #FIXME verify feed has items
        #cleanup
        for x in searches.keys():
            mirolib.delete_feed(self,reg,x)


    def test_80(self):

        """http://litmus.pculture.org/show_test.cgi?id=80 Search - New Search Channel: URL
        1.Select Sidebar -> New Search Podcast
        2.Enter the search term: MP3
        3.Select the URL radio button and enter, http://www.ubu.com in the text box
        4.Click Create Podcast
        5.In the warning dialog - click Yes.
        """

        reg = mirolib._AppRegions()
        source = "http://www.ubu.com"
        term =  "mp3"
        search_term = "Gertrude"
        radio = "URL"
        mirolib.new_search_feed(self,reg,term,radio,source,defaults=False,watched=False)
        if exists("compatible",45):
            type(Key.ENTER)
        time.sleep(30)  # scraping takes a while - need to wait before confirming element present.
        mirolib.click_sidebar_tab(self,reg,"Podcasts")
        mirolib.tab_search(self,reg,search_term,confirm_present=True)
        mirolib.delete_feed(self,reg,term)  


    def test_79(self):
        """http://litmus.pculture.org/show_test.cgi?id=79 Search - New Search Podcast: Engine
        Steps to Perform:

        1.  Select Sidebar -> New Search Podcast
        2.  Enter a search term
        3.  Select the Search Engine radio button
        4.  Select a search engine from the pulldown menu
        5.  Select Create Podcast
        """

        reg = mirolib._AppRegions()
        source_array = { "Yahoo": "Canada", "DailyMotion": "Ontario", "Video": "toronto"}
        radio = "Search"
        for source, term in source_array.iteritems():
            mirolib.new_search_feed(self,reg,term,radio,source,defaults=False,watched=False)
            mirolib.click_podcast(self,reg,source)
            mirolib.shortcut("r")
            mirolib.confirm_download_started(self,reg,term)  

        #FIXME verify feed has items
        #cleanup
        for x in source_array.keys():
            mirolib.delete_feed(self,reg,x)
   
# Post the output directly to Litmus
if __name__ == "__main__":
    import LitmusTestRunner
    print len(sys.argv)
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv,config.testlitmus).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(Miro_Suite,config.testlitmus).litmus_test_run()
   


