"""
Contains methods for making comparisions using a host of tests.
They are also for modifying a glyph by altering its 
serif, stroke , stem thickness, size, italic angle etc.
and then later producing scores by doing bitmap comparision
"""
from fc.GlyphCompare import GlyphCompare

class FontCompare(object):
    ascentScore = 0
    descentScore = 0
    capHeightScore = 0
    isCIDCompare = False
    quadraticOrCubicScore = 0
    strokeWidthScore = -1
    uposScore = 0
    uwidthScore = 0
    weightScore = 0
    xHeightScore = -1
    pureBitmapScore = -1

    def font_facecompare(self, Testfont, Standardfont, glyphRange, \
    resolution, ptsize, pixeldepth, gtype):
        if gtype is "italic":
            Testfont.selection.all()
            Standardfont.selection.all()
            italicTest = Testfont.italicize(-13)
            italicStandard = Standardfont.italicize(-13)
        scores = list()
        comparator = GlyphCompare()
        pixelsize = (resolution*ptsize)/72
        for unicode_value in range (glyphRange[0],glyphRange[1]):
            if unicode_value in Standardfont:
                if unicode_value in Testfont:
                    comparator.initialise(pixelsize,pixeldepth)
                    glyphname=Standardfont[unicode_value].glyphname
                    if gtype is "normal" or "italic":
                        glyphscore=comparator.basicbitmapScore \
                        (Standardfont[unicode_value], \
                        Testfont[unicode_value])
                    if gtype is "bold":
                        glyphscore=comparator.boldbitmapScore \
                        (Standardfont[unicode_value], \
                        Testfont[unicode_value])
                    scores.append((glyphname,round(glyphscore)))
        return scores
