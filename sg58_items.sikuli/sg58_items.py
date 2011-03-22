import sys
import os
import glob
import unittest
import StringIO
import time

mycwd = os.path.join(os.getenv("PCF_TEST_HOME"),"Miro")
sys.path.append(os.path.join(mycwd,'myLib'))
import config
import mirolib
import testvars
import litmusresult



setBundlePath(config.get_img_path())


class Miro_Suite(unittest.TestCase):
    """Subgroup 41 - one-click subscribe tests.

    """
    def setUp(self):
        self.verificationErrors = []
        setAutoWaitTimeout(60)
         


    def test_361(self):
        """http://litmus.pculture.org/show_test.cgi?id=361 edit item audio to video.

        1. add 3-blip-videos feed
        2. download the Joo Joo
        3. Edit item from Video to Audio
        4. Verify item played as audio item

        """
        reg = mirolib.AppRegions()
        
        url = "http://pculture.org/feeds_test/3blipvideos.xml"
        feed = "blip"
        item_title = "Joo Joo"
        #add feed and download joo joo item
        mirolib.add_feed(self,reg,url,feed)
        reg.s.click(feed)
        mirolib.tab_search(self,reg,item_title)
        reg.m.click("Download")
        mirolib.wait_download_complete(self,reg,item_title)
        #find item in video tab and edit to audio
        mirolib.click_sidebar_tab(self,reg,"Video")
        mirolib.tab_search(self,reg,item_title,confirm_present=True)
        reg.m.click(item_title)
        reg.t.click("File")
        reg.t.click("Edit")
        reg.m.click("Audio")
        reg.m.click("Apply")
        #locate item in audio tab and verify playback
        mirolib.click_sidebar_tab(self,reg,"Music")
        mirolib.tab_search(self,reg,item_title,confirm_present=True)
        m.doubleClick(item_title)
        mirolib.verify_audio_playback(self,reg)
        #cleanup
        mirolib.delete_feed(self,reg,"blip")
 
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        
        
# Post the output directly to Litmus
if config.testlitmus == True:
    suite_list = unittest.getTestCaseNames(Miro_Suite,'test')
    suite = unittest.TestSuite()
    for x in suite_list:
        suite.addTest(Miro_Suite(x))

    buf = StringIO.StringIO()
    runner = unittest.TextTestRunner(stream=buf)
    litmusresult.write_header(config.get_os_name())
    for x in suite:
        runner.run(x)
        # check out the output
        byte_output = buf.getvalue()
        id_string = str(x)
        stat = byte_output[0]
        try:
            print "writing log"
            litmusresult.write_log(id_string,stat,byte_output)
        finally:
            buf.truncate(0)
    litmusresult.write_footer()
#or just run it locally
else:
    unittest.main()
