from fc.BitmapHandler import CreateSpriteSheet
from fc.GlyphConsistency import GlyphConsistency
import shelve
gcy = GlyphConsistency()
class MockGlyph:
    bbox = list()
    worthy = 0
    selfintersects = 0
    layercnt = 0
    rbearing = 0
    lbearing = 0
    roundconsistent=0
    def __init__(self,glyph):
        self.worthy = glyph.isWorthOutputting()
        self.selfintersects = glyph.layers[1].selfIntersects()
        self.layercnt = glyph.layer_cnt
        self.lbearing = glyph.left_side_bearing
        self.rbearing = glyph.right_side_bearing
        self.bbox.append(glyph.boundingBox()[0])
        self.bbox.append(glyph.boundingBox()[1])
        self.bbox.append(glyph.boundingBox()[2])
        self.bbox.append(glyph.boundingBox()[3])
        self.roundconsistent = gc.GlyphCompare(glyph)

class MockFont:
    ascent=0
    descent=0
    strokewidth=0
    upos=0
    xheight=0
    glyphs = list()
    normalglyphfile = "../data/masterspritenormal.bmp"
    boldglyphfile = "../data/masterspritebold.bmp"
    italicglyphfile = "../data/masterspriteitalic.bmp"
    def __init__(self,font,pixelsize,glyphrange):
        self.ascent = font.ascent
        self.descent = font.descent
        self.upos = font.upos
        self.xheight = font.xheight
        #normal 
        t=CreateSpriteSheet(pixelsize,font,glyphrange,"normal")
        #bold
        t=CreateSpriteSheet(pixelsize,font,glyphrange,"bold")
        #italic
        t=CreateSpriteSheet(pixelsize,font,glyphrange,"italic")
"""
class Mockify:
    def __init__(self,font,mockfilename,glyphrange,pixelsize):
        mock_font = shelve.open("../data/"+mockfilename+".mcy")
        mock_font["font"] = MockFont(font,pixelsize,glyphrange) 
        mock_font.close()
"""
