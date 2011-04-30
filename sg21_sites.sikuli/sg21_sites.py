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
import mirolib
import testvars
import base_testcase

class Miro_Suite(base_testcase.Miro_unittest_testcase):
    """Subgroup 41 - one-click subscribe tests.

    """
    def test_182(self):
        """http://litmus.pculture.org/show_test.cgi?id=182 dl from youtube site.

        1. Open youtube url as site
        2. download button
        3. verify download started
        4. Cleanup
        """
        site_url = "http://www.youtube.com/watch?v=fgg2tpUVbXQ&feature=channel"
        site = "YouTube"
        
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        dl_this = testvars.youtube_download_this(self)
        reg.mtb.find(dl_this)
        self.assertTrue(reg.mtb.exists(dl_this))
        reg.mtb.click(dl_this)
        mirolib.confirm_download_started(self,reg,"Deep")
        mirolib.delete_site(self,reg,site)

    def test_194(self):
        """http://litmus.pculture.org/show_test.cgi?id=194 rename source.

        1. Add blip.tv as a source
        2. rename
        3. restart and verify name persists
        4. Cleanup
        """
        site_url = "http://blip.tv"
        site = "blip"
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        reg.t.click("Sidebar")
        reg.t.click("Rename")
        time.sleep(3)
        type("BLIP TV ROCKS \n")
        self.assertTrue(reg.s.exists("BLIP TV ROCKS"))

        mirolib.quit_miro(self,reg)
        reg = mirolib.AppRegions()
        self.assertTrue(reg.s.exists("BLIP"))
        mirolib.delete_site(self,reg,"BLIP")


    def stest_39(self):
        """http://litmus.pculture.org/show_test.cgi?id=39 site navigation.


        #skipping for now will fix later.
        
        1. Add blip.tv as a source
        2. navigate through site
        3. verify nav buttons and states
        4. Cleanup
        """
        site_url = "http://blip.tv"
        site = "blip"
        reg = mirolib.AppRegions()
        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        time.sleep(10)

        find("navstop_disabled.png")
        find("navforward_disabled.png")
        find("navhome.png")
        find("navreload.png")

        reg.m.click(testvars.blip_browse)
        reg.m.click(testvars.blip_recent)
        self.assertTrue(reg.mtb.exists("navback.png"))
        self.assertTrue(reg.mtb.exists("navforward_disabled.png"))
        self.assertTrue(reg.mtb.exists("navhome.png"))
        self.assertTrue(reg.mtb.exists("navreload.png"))

        reg.mtb.click("navback.png")
        self.assertTrue(reg.mtb.exists("navforward.png"))
        self.assertTrue(reg.mtb.exists("navback_disabled.png"))
        self.assertTrue(reg.mtb.exists("navhome.png"))
        self.assertTrue(reg.mtb.exists("navreload.png"))

        reg.mtb.click("navforward")
        self.assertTrue(reg.mtb.exists("navback.png"))
        self.assertTrue(reg.mtb.exists("navforward_disabled.png"))
        self.assertTrue(reg.mtb.exists("navhome.png"))
        self.assertTrue(reg.mtb.exists("navreload.png"))
        
        reg.mtb.click("navreload.png")
        reg.mtb.click("navstop.png")
        self.assertTrue(reg.mtb.exists("navback.png"))
        self.assertTrue(reg.mtb.exists("navforward.png"))
        self.assertTrue(reg.mtb.exists("navhome.png"))
        self.assertTrue(reg.mtb.exists("navreload.png"))

        reg.mtb.click("navhome.png")
        #FIX MEwait for the updating icon to appear then disappear
        self.assertTrue(reg.mtb.exists("navback.png"))
        self.assertTrue(reg.mtb.exists("navforward_disabled.png"))
        self.assertTrue(reg.mtb.exists("navhome.png"))
        self.assertTrue(reg.mtb.exists("navreload.png"))
        



        mirolib.delete_site(self,reg,site)
        

    def test_191(self):
        """http://litmus.pculture.org/show_test.cgi?id=191 Add rss feed to sidebar.

        1. Addbits.net as a source
        2. Open Netlabel Music page and add RSS feed
        3. Verify feed added to the sidebar
        4. Cleanup
        """
        site_url = "http://clearbits.net"
        site = "ClearBits"
        reg = mirolib.AppRegions()
        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        reg.m.click("Netlabel Music")
        reg.m.click(testvars.clearbits_rss)
        p = mirolib.get_podcasts_region(reg)
        time.sleep(3)
        self.assertTrue(p.exists("ClearBits"))
        mirolib.delete_feed(self,reg,"ClearBits")
        mirolib.delete_site(self,reg,"ClearBits")


    def test_193(self):
        """http://litmus.pculture.org/show_test.cgi?id=193 torrent direct dl.

        1. Add clearbits.net page as a source
        2. click to dl the torrent file
        3. Verify file starts to download
        4. Cleanup
        """
        site_url = "http://www.clearbits.net/torrents/662-here-be-dragons-ipod"
        site = "ClearBits"
        title = "Dragons"
                        
        setAutoWaitTimeout(60)
        reg = mirolib.AppRegions()
        mirolib.cancel_all_downloads(self,reg)

        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        reg.m.click("Torrent file")
        mirolib.confirm_download_started(self,reg,title)

        mirolib.delete_items(self,reg,title,"Downloading")
        mirolib.delete_site(self,reg,"ClearBits")


    def test_192(self):
        """http://litmus.pculture.org/show_test.cgi?id=192 file detection dl.

        1. Add clearbits.net page as a source
        2. click to dl the torrent file
        3. Verify file starts to download
        4. Cleanup
        """
        site_url = "http://pculture.org/feeds_test/http-direct-downloads.html"
        site = "HTTP Direct"
        HTTPDOWNLOADS = {".mpeg download":"mighty",
                         ".ogv download":"popeye",
                         ".mp4 download":"big",
                         ".mov download":"Matrix",
                         ".wmv download":"WindowsMedia",
                         ".avi download":"Coyote",
                         ".mpg download":"dothack2",
                         ".mkv download 2":"mulitple",
                         ".ogg download":"gd",
                         ".mp3 download":"gd",
                         ".wma download":"Bangles",
                         ".m4a download":"luckynight",
                         ".flac download":"luckynight",
                         ".mka download":"Widow",
                         }
        setAutoWaitTimeout(60) 
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        reg.s.click(site)
        for filetype, title in HTTPDOWNLOADS.iteritems():
            try:
                if reg.m.exists(filetype):
                    click(reg.m.getLastMatch())
                else:
                    type(Key.PAGE_DOWN)
                    reg.m.find(filetype)
                    click(reg.m.getLastMatch())
                mirolib.confirm_download_started(self,reg,title)
                mirolib.delete_items(self,reg,title,"downloading")
                mirolib.click_source(self,reg,site)
            except:
                self.verificationErrors.append("download failed for imagetype" +str(filetype))
                
        mirolib.delete_site(self,reg,site)
        mirolib.cancel_all_downloads(self,reg)

    def test_321(self):
        """http://litmus.pculture.org/show_test.cgi?id=321 delete slow to load site.

        1. Add slow feed as a source
        2. delete it before is loads
        """
        site_url = "http://pculture.org/feeds_test/slowsite.php"
        site = "pculture"
        
        setAutoWaitTimeout(60)                
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        mirolib.delete_site(self,reg,site)

    def test_195(self):
        """http://litmus.pculture.org/show_test.cgi?id=196 delete site.

        1. Add header test as a source
        2. delete it 
        """
        site_url = "http://pculture.org/feeds_test/header-test.php"
        site = "Header Test"
        setAutoWaitTimeout(60)                
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        mirolib.delete_site(self,reg,site)

    def test_194(self):
        """http://litmus.pculture.org/show_test.cgi?id=194 site with non-utf-8 chars.

        1. Add http://diziizle.net/
        2. Verify added
        3. Restart and verify still there
        4. Cleanup
        """
        
        site_url = "http://diziizle.net/"
        site = "diziizle"
        setAutoWaitTimeout(60)                
        reg = mirolib.AppRegions()
        mirolib.add_source(self,reg,site_url,site)
        mirolib.click_source(self,reg,site)
        reg.m.find(testvars.dizizle_logo)
        mirolib.quit_miro(self,reg)
        mirolib.restart_miro(self,reg)
        mirolib.click_source(self,reg,site)
        self.assertTrue(reg.m.exists(testvars.dizizle_logo))    
        mirolib.delete_site(self,reg,site)


    def test_143(self):
        """http://litmus.pculture.org/show_test.cgi?id=143 multiple delete and cancel.

        1. Add clearbits and archive.org
        2. select bogh and delete, the cancel
        3. verify sites not deleted.
        4. Cleanup
        """
        site_url = "http://clearbits.net"
        site_url2 = "http://archive.org"
        site = "ClearBits"
        site2 = "Internet"
        setAutoWaitTimeout(60)
        reg = mirolib.AppRegions()

        mirolib.add_source(self,reg,site_url,site)
        mirolib.add_source(self,reg,site_url2,site2)
        p = mirolib.get_sources_region(reg)
        p.click(site)
        keyDown(Key.SHIFT)
        p.click(site2)
        keyUp(Key.SHIFT)
        self.assertTrue(reg.m.exists("button_mv_delete_all.png"))
        click(reg.m.getLastMatch())
        mirolib.remove_confirm(self,reg,"cancel")
        p = mirolib.get_sources_region(reg)
        self.assertTrue(p.exists(site))
        self.assertTrue(p.exists(site2))

        #Cleanup
        mirolib.delete_site(self,reg,site)
        mirolib.delete_site(self,reg,site2)
        
# Post the output directly to Litmus
if __name__ == "__main__":
    import LitmusTestRunner
    print len(sys.argv)
    if len(sys.argv) > 1:
        LitmusTestRunner.LitmusRunner(sys.argv,config.testlitmus).litmus_test_run()
    else:
        LitmusTestRunner.LitmusRunner(Miro_Suite,config.testlitmus).litmus_test_run()
   




