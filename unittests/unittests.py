from fc.GlyphCompare import GlyphCompare
from fc.FontCompare import FontCompare
from fc.BitmapHandler import BitmapCompare
from fc.GlyphConsistency import GlyphConsistency
import unittest
import fontforge
testfont = fontforge.open("unittests/lohit.ttf")
class Basictests(unittest.TestCase):
    def testGlyphCompare(self):
        cm = GlyphCompare()
        cm.initialise(10,1)
        test0 = 0
        if cm.Pixels == 10 and cm.Pixeldepth == 1:
            test0 = 1
        self.failUnless(test0)
        test1 = cm.basicbitmapScore(testfont[0x930],testfont[0x931])
        test2 = cm.bearingScore(testfont[0x930],testfont[0x931])
        test3 = cm.boldbitmapScore(testfont[0x930],testfont[0x931])
        test1 = (0 <= test1 <= 100)
        self.failUnless(test1)
        test2 = (0 <= test2 <= 10)
        self.failUnless(test2)
        test3 = (0 <= test3 <= 100)
        self.failUnless(test3)

    def testFontCompare(self):
        cm = FontCompare()
        basic = cm.font_basiccompare(testfont,testfont)
        bastest=1
        for tup in basic:
            if tup[1]!=10:
                bastest=0
        self.failUnless(bastest)
        bold = cm.font_facecompare(testfont,testfont,(0x901,0x970),\
        600,12,1,"bold") 
        italic = cm.font_facecompare(testfont,testfont,(0x901,0x970),\
        600,12,1,"italic") 
        normal = cm.font_facecompare(testfont,testfont,(0x901,0x970),\
        600,12,1,"normal") 
        test = 1
        total1 = 0
        for tup in bold:
            if tup[1]!=100:
                test1=0
            total1+=1
        self.failUnless(test)
        total2 = 0
        test = 1
        for tup in italic:
            if tup[1]!=100:
                test=0
            total2+=1
        self.failUnless(test)
        total3 = 0
        test = 1
        for tup in normal:
            if tup[1]!=100:
                test=0
            total3+=1
        self.failUnless(test)
        test = 0
        if total1 == total2 == total3:
            test = 1
        self.failUnless(test)

    def testGlyphConsistency(self):
        cm = GlyphConsistency()
        test1 = cm.glyph_basicConsistency(testfont,(0x930,0x931))
        test2 = cm.glyph_basicset_consistency(testfont,(0x901,0x970))
        test3 = cm.glyph_round_consistency(testfont,(0x901,0x970))
        test = (0 <= test1[0][1] <= 10)
        self.failUnless(test)
        test2 = (0 <= test2 <= 10)
        self.failUnless(test2)
        test = (0 <= test3 <= 10)
        self.failUnless(test3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
