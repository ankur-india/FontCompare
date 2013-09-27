from fc.FontCompare import FontCompare
from fc.BitmapHandler import BitmapCompare
from fc.GlyphConsistency import GlyphConsistency
from fc.mockify import MockFont
import shelve
import pkg_resources
import shutil
import unittest
import fontforge
#load the mockfonts for testing
thefile = pkg_resources.resource_filename("fc","data/mockfile.mcy")
shutil.copy(thefile,"/var/tmp/tmp.mcy")
mock_font = shelve.open("/var/tmp/tmp.mcy")
mockfont = mock_font["font"]
mock_font.close()

class Basictests(unittest.TestCase):
    def testFontCompare(self):
        cm = FontCompare()
        testfont = fontforge.open("unittests/lohit.ttf")
        basic = cm.font_basiccompare(testfont,mockfont)
        bastest=1
        for tup in basic:
            if tup[1]!=10:
                bastest=0
        self.failUnless(bastest)
        testfont = fontforge.open("unittests/lohit.ttf")
        bold = cm.font_facecompare(testfont,mockfont,(0x900,0x97f),\
        600,12,1,"bold")
        testfont = fontforge.open("unittests/lohit.ttf")
        italic = cm.font_facecompare(testfont,mockfont,(0x900,0x97f),\
        600,12,1,"italic")
        testfont = fontforge.open("unittests/lohit.ttf")
        normal = cm.font_facecompare(testfont,mockfont,(0x900,0x97f),\
        600,12,1,"normal")
        test = 1
        print len(normal)
        for tup in bold:
            if tup[1]==100 or tup[1]==0:
                test1=1
                break
        self.failUnless(test)
        test = 0
        for tup in italic:
            if tup[1]==100 or tup[1]==0:
                test=1
                break
        self.failUnless(test is 1)
        test = 0
        for tup in normal:
            if tup[1]==100 or tup[1]==0:
                test=1
                break
        self.failUnless(test is 1)
        test = 0
        if len(normal) == len(bold) == len(italic):
            test = 1
        self.failUnless(test is 1)

    def testGlyphConsistency(self):
        cm = GlyphConsistency()
        testfont = fontforge.open("unittests/lohit.ttf")
        test1 = cm.glyph_basicConsistency(testfont,(0x900,0x97f))
        testfont = fontforge.open("unittests/lohit.ttf")
        test2 = cm.glyph_basicset_consistency(testfont,(0x900,0x97f))
        testfont = fontforge.open("unittests/lohit.ttf")
        test3 = cm.glyph_round_consistency(testfont,(0x900,0x97f),50)

        test = (0 <= test1[0][1] <= 10)
        self.failUnless(test)
        test2 = (0 <= test2 <= 10)
        self.failUnless(test2)
        test3 = (0 <= test3 <= 10)
        self.failUnless(test3)

"""
unittests for DocCompare not required.
"""
def main():
    unittest.main()

if __name__ == '__main__':
    main()
