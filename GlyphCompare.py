import fontforge
from BitmapCompare import *

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
        Testglyph.export("test.bmp",self.Pixels,self.Pixeldepth)
        Standardglyph.export("standard.bmp",self.Pixels,self.Pixeldepth)
        return self.bm.basicCompare("test.bmp","standard.bmp")

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
