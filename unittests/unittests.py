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
