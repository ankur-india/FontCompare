import os
from fc.BitmapHandler import BitmapCompare
import shutil
import pkg_resources

class DocCompare:
    def basicCompare(self,testpath, mockfont, fontsize):
        docpath = pkg_resources.resource_filename("fc","docs/doc.txt")
        bashcommand = "hb-view --output-format=\"png\" --output-file=\"/var/tmp/test.png\" --font-size="+str(fontsize)+" --text-file=\""
        bashcommand+=docpath+"\" "+"\""+testpath+"\""
        os.system(str(bashcommand))
        print bashcommand
        thefile = pkg_resources.resource_filename("fc",mockfont.highresdocfile)
        shutil.copy(thefile,"/var/tmp/standard.png")
        cm = BitmapCompare()
        score = cm.basicCompare("/var/tmp/test.png",\
        "/var/tmp/standard.png",1000,0,True)
        return score
