from fc.BitmapHandler import CreateSpriteSheet
import shelve
import fontforge

class MockFont:
    ascent=0
    descent=0
    strokewidth=0
    uwidth=0
    upos=0
    xHeight=0
    glyphs = list()
    capHeight=0
    normalglyphfile = "data/masterspritenormal.bmp"
    boldglyphfile = "data/masterspritebold.bmp"
    italicglyphfile = "data/masterspriteitalic.bmp"
    def __init__(self,fontpath,pixelsize,glyphrange):
        font = fontforge.open(fontpath)
        self.ascent = font.ascent
        self.descent = font.descent
        self.upos = font.upos
        self.uwidth = font.uwidth
        self.xHeight = font.xHeight
        self.capHeight = font.capHeight
        #normal 
        CreateSpriteSheet(pixelsize,font,glyphrange,"normal")
        font = fontforge.open(fontpath)
        #bold
        CreateSpriteSheet(pixelsize,font,glyphrange,"bold")
        font  = fontforge.open(fontpath)
        #italic
        CreateSpriteSheet(pixelsize,font,glyphrange,"italic") 
"""
class Mockify:
    def __init__(self,font,mockfilename,glyphrange,pixelsize):
        mock_font = shelve.open("../data/"+mockfilename+".mcy")
        mock_font["font"] = MockFont(font,pixelsize,glyphrange) 
        mock_font.close()
"""
