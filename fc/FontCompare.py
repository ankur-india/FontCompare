"""
Contains methods for making comparisions using a host of tests.
They are also for modifying a glyph by altering its 
serif, stroke , stem thickness, size, italic angle etc.
and then later producing scores by doing bitmap comparision
"""
from fc.GlyphCompare import *

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

    def font_facecompare(self, Testfont, Standardfont, glyphRange, resolution, ptsize, pixeldepth, gtype):
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
                        glyphscore=comparator.basicbitmapScore(Standardfont[unicode_value], Testfont[unicode_value])
                    if gtype is "bold":
                        glyphscore=comparator.boldbitmapScore(Standardfont[unicode_value], Testfont[unicode_value])
                    scores.append((glyphname,round(glyphscore)))
        return scores

class FontOS2Compare(object):
    os2_codepagesScore = ()	#A 2 element tuple containing the OS/2 Codepages field
    os2_family_classScore=0
    os2_fstypeScore=0
    os2_panoseScore=0
    os2_strikeyposScore=0
    os2_strikeysizeScore=0
    os2_subxoffScore=0
    os2_subxsizeScore=0
    os2_subyoffScore=0
    os2_subysizeScore=0
    os2_supxoffScore=0
    os2_supxsizeScore=0
    os2_supyoffScore=0
    os2_supysizeScore=0
    os2_typoascentScore=0
    os2_typoascent_addScore=0
    os2_typodescentScore=0
    os2_typodescent_addScore=0
    os2_typolinegapScore=0
    os2_use_typo_metricsScore=0
    os2_unicoderangesScore =()	#A 4 element tuple containing the OS/2 Unicode Ranges field
    os2_vendorScore=0
    os2_versionScore=0
    os2_weightScore=0
    os2_weight_width_slope_onlyScore=0
    os2_widthScore=0
    os2_winascentScore=0
    os2_winascent_addScore=0
    os2_windescentScore=0
    os2_windescent_addScore=0
