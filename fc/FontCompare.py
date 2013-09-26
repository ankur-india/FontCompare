"""
Contains methods for making comparisions using a host of tests.
They are also for modifying a glyph by altering its 
serif, stroke , stem thickness, size, italic angle etc.
and then later producing scores by doing bitmap comparision
"""
from fc.BitmapHandler import BitmapCompare
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

    def font_basiccompare(self, Testfont, mockfont):
        final=list()
<<<<<<< HEAD
        
        mx=max(Testfont.ascent,mockfont.ascent)
        mn=min(Testfont.ascent,mockfont.ascent)
        score1 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Ascent Score: ",score1))
        
        mx=max(Testfont.descent,mockfont.descent)
        mn=min(Testfont.descent,mockfont.descent)
        score2 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Descent Score: ",score2))
        
        mx=max(Testfont.capHeight,mockfont.capHeight)
        mn=min(Testfont.capHeight,mockfont.capHeight)
        score3 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Cap Height: ",score3))
        
        mx=max(Testfont.strokewidth,mockfont.strokewidth)
        mn=min(Testfont.strokewidth,mockfont.strokewidth)
        score4 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Stroke Width Score: ",score4))
        
        mx=max(Testfont.upos,mockfont.upos)
        mn=min(Testfont.upos,mockfont.upos)
        score5 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Underline Position Score: ",score5))
        
        mx=max(Testfont.uwidth,mockfont.uwidth)
        mn=min(Testfont.uwidth,mockfont.uwidth)
        score6 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("Underline Width Score: ",score6))
        
        mx=max(Testfont.xHeight,mockfont.xHeight)
        mn=min(Testfont.xHeight,mockfont.xHeight)
        score7 = int((1/float(abs(mx-mn)))*10) if (mx-mn)!=0 else 10
        final.append(("x Height Score: ",score7))
        
        test=Testfont.weight
        standard=mockfont.weight
        score8 = 10 if test==standard else 0
        final.append(("PostScript weight string",score8))
        
        score=score1+score2+score3+score4+score5+score6+score7+score8;
        final.append(("Average Basic Score: ",score/8.0))
        Testfont.close()
        return final

    def font_facecompare(self, Testfont, mockfont, glyphRange, \
    resolution, ptsize, pixeldepth, fonttype):
        spritepath = "/var/tmp/tmpn.bmp"
        if fonttype is "bold":
            spritepath = "/var/tmp/tmpb.bmp"
            for i in range (glyphRange[0],glyphRange[1]):
                if i in Testfont:
                    Testfont[i].changeWeight(50,"auto",0,0,"auto")
=======
        mx=max(Testfont.ascent,Standardfont.ascent)
        mn=min(Testfont.ascent,Standardfont.ascent)
        score1 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Ascent Score: ",score1))
        mx=max(Testfont.descent,Standardfont.descent)
        mn=min(Testfont.descent,Standardfont.descent)
        score2 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Descent Score: ",score2))
        mx=max(Testfont.capHeight,Standardfont.capHeight)
        mn=min(Testfont.capHeight,Standardfont.capHeight)
        score3 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Descent Score: ",score3))
        mx=max(Testfont.strokewidth,Standardfont.strokewidth)
        mn=min(Testfont.strokewidth,Standardfont.strokewidth)
        score4 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Stroke Width Score: ",score4))
        mx=max(Testfont.upos,Standardfont.upos)
        mn=min(Testfont.upos,Standardfont.upos)
        score5 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Underline Position Score: ",score5))
        mx=max(Testfont.uwidth,Standardfont.uwidth)
        mn=min(Testfont.uwidth,Standardfont.uwidth)
        score5 = (1/float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("Underline Width Score: ",score5))
        mx=max(Testfont.xHeight,Standardfont.xHeight)
        mn=min(Testfont.xHeight,Standardfont.xHeight)
        score6 = 1/(float(abs(mx-mn)))*10 if (mx-mn)!=0 else 10
        final.append(("x Height Score: ",score6))
        score=score1+score2+score3+score4+score5+score6
        final.append(("Average Basic Score: ",score/6.0))
        Testfont.close()
        if Testfont != Standardfont:
            Standardfont.close()
        return final

    def font_facecompare(self, Testfont, Standardfont, glyphRange, \
    resolution, ptsize, pixeldepth, fonttype):
>>>>>>> 2466c64... simplified the code and fixed tests with erroneous results.
        if fonttype is "italic":
            Testfont.selection.all()
            Testfont = Testfont.italicize(-13)
            spritepath = "/var/tmp/tmpi.bmp"
        scores = list()
        comparator = BitmapCompare()
        pixelsize = (resolution*ptsize)/72
<<<<<<< HEAD
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
=======
        for unicode_value in range (glyphRange[0],glyphRange[1]):
            glyphscore = 0
            if unicode_value in Standardfont:
                if unicode_value in Testfont:
                    comparator.initialise(pixelsize,pixeldepth)
                    if fonttype is "normal" or "italic":
                        glyphscore=comparator.basicbitmapScore \
                        (Standardfont[unicode_value], \
                        Testfont[unicode_value])
                    if fonttype is "bold":
                        glyphscore=comparator.boldbitmapScore \
                        (Standardfont[unicode_value], \
                        Testfont[unicode_value])
            scores.append((str(hex(unicode_value))+" ",round(glyphscore)))
        Testfont.close()
        if Testfont != Standardfont:
            Standardfont.close()
>>>>>>> 2466c64... simplified the code and fixed tests with erroneous results.
        return scores
