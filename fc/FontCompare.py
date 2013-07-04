"""
Contains methods for making comparisions using a host of tests.
They are also for modifying a glyph by altering its 
serif, stroke , stem thickness, size, italic angle etc.
and then later producing scores by doing bitmap comparision
"""
from fc.BitmapHandler import BitmapCompare
from fc.GlyphCompare import GlyphCompare
from fc.mockify import MockFont
import shutil
import pkg_resources
thefile = pkg_resources.resource_filename("fc","data/masterspritebold.bmp")
shutil.copy(thefile,"/var/tmp/tmpb.bmp")
thefile = pkg_resources.resource_filename("fc","data/masterspritenormal.bmp")
shutil.copy(thefile,"/var/tmp/tmpn.bmp")
thefile = pkg_resources.resource_filename("fc","data/masterspriteitalic.bmp")
shutil.copy(thefile,"/var/tmp/tmpi.bmp")
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
        final.append(("Cap Height: ",score3))
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
        return final;

    def font_facecompare(self, Testfont, mockfont, glyphRange, \
    resolution, ptsize, pixeldepth, fonttype):
        spritepath = "/var/tmp/tmpn.bmp"
        if fonttype is "bold":
            spritepath = "/var/tmp/tmpb.bmp"
            for i in range (glyphRange[0],glyphRange[1]):
                if i in Testfont:
                    Testfont[i].changeWeight(50,"auto",0,0,"auto")
        if fonttype is "italic":
            Testfont.selection.all()
            Testfont = Testfont.italicize(-13)
            spritepath = "/var/tmp/tmpi.bmp"
        scores = list()
        comparator = BitmapCompare()
        pixelsize = (resolution*ptsize)/72
        print spritepath
        for i in range (glyphRange[0],glyphRange[1]):
            if i in Testfont:
                Testfont[i].export("/var/tmp/tmp.bmp",pixelsize,1)
                Testfont[i].export("tmp.bmp",pixelsize,1)
                glyphscore = comparator.basicCompare("/var/tmp/tmp.bmp",\
                spritepath,pixelsize,(i-glyphRange[0])*pixelsize)
                glyphscore*=100
            else:
                glyphscore=0
            scores.append((str(hex(i))+" ",round(glyphscore)))
        Testfont.close()
        return scores
