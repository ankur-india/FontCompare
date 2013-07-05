"""
Contains methods for making comparisions using a host of tests.
They are also for modifying a glyph by altering its 
serif, stroke , stem thickness, size, italic angle etc.
and then later producing scores by doing bitmap comparision
"""
from fc.GlyphCompare import GlyphCompare

class FontCompare(object):

    def font_basiccompare(self, Testfont, Standardfont):
        final=list()
        mx=max(Testfont.ascent,Standardfont.ascent);
        mn=min(Testfont.ascent,Standardfont.ascent);
        score1 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Ascent Score: ",score1))
        mx=max(Testfont.descent,Standardfont.descent);
        mn=min(Testfont.descent,Standardfont.descent);
        score2 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Descent Score: ",score2))
        mx=max(Testfont.capHeight,Standardfont.capHeight);
        mn=min(Testfont.capHeight,Standardfont.capHeight);
        score3 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Descent Score: ",score3))
        mx=max(Testfont.strokewidth,Standardfont.strokewidth);
        mn=min(Testfont.strokewidth,Standardfont.strokewidth);
        score4 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Stroke Width Score: ",score4))
        mx=max(Testfont.upos,Standardfont.upos);
        mn=min(Testfont.upos,Standardfont.upos);
        score5 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Underline Position Score: ",score5))
        mx=max(Testfont.uwidth,Standardfont.uwidth);
        mn=min(Testfont.uwidth,Standardfont.uwidth);
        score5 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("Underline Width Score: ",score5))
        mx=max(Testfont.xHeight,Standardfont.xHeight);
        mn=min(Testfont.xHeight,Standardfont.xHeight);
        score6 = 1/(float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10;
        final.append(("x Height Score: ",score6))
        score=score1+score2+score3+score4+score5+score6;
        final.append(("Average Basic Score: ",score/6.0))
        Testfont.close()
        Standardfont.close()
        return final;

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
        Testfont.close()
        Standardfont.close()
        return scores
