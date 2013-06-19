import fontforge
from fc.BitmapCompare import *

class GlyphCompare(object):
    Pixels = 10
    Pixeldepth = 1
    bm = BitmapCompare()
    #kerning parameters if any
    #tex parameters if any
    #hint parameters if any
    def initialise(self,pixels, pixeldepth):
        self.Pixels = pixels
        self.Pixeldepth = pixeldepth

    def basicbitmapScore(self,Testglyph,Standardglyph):
        Testglyph.export("/var/tmp/test.bmp",self.Pixels,self.Pixeldepth)
        Standardglyph.export("/var/tmp/standard.bmp",self.Pixels,self.Pixeldepth)
        return self.bm.basicCompare("/var/tmp/test.bmp","/var/tmp/standard.bmp")

    def bearingScore(self,Testglyph,Standardglyph):
        parlA = Standardglyph.left_side_bearing
        parlB = Testglyph.left_side_bearing
        parrA = Standardglyph.right_side_bearing
        parrB = Testglyph.right_side_bearing
        ansl = min(abs(parlA-parlB),abs(parlB-parlA))
        ansr = min(abs(parrA-parrB),abs(parrB-parrA))
        if ansl:
            ansl = (1/float(ansl))*10
        if ansr:
            ansr = (1/float(ansr))*10
        return round((ansl+ansr)/2)

    def boldbitmapScore(self,Testglyph,Standardglyph):
        squishTestglyph=Testglyph
        squishTestglyph.changeWeight(50,"auto",0,0,"squish")
        Testglyph.changeWeight(50,"auto",0,0,"auto")
        squishStandardglyph=Standardglyph
        squishStandardglyph.changeWeight(50,"auto",0,0,"squish")
        Standardglyph.changeWeight(50,"auto",0,0,"auto")
        score1 = self.basicbitmapScore(squishTestglyph,squishStandardglyph)
        score2 = self.basicbitmapScore(Testglyph,Standardglyph)
        return float(score1+score2)/2
    
    #def strokebitmapcompare(self, glyph, linecap, linejoin, flags):
