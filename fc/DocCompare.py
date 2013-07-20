import os
from fc.BitmapHandler import BitmapCompare
class DocCompare:
    def basicCompare(self,testpath, standardpath, docpath, fontsize):
        bashcommand = "hb-view --output-format=\"png\" --output-file=\"/var/tmp/test.png\" --font-size="+str(fontsize)+" --text-file=\""
        bashcommand+=docpath+"\" "+"\""+testpath+"\""
        print bashcommand
        os.system(str(bashcommand))
        
        bashcommand = "hb-view --output-format=\"png\" --output-file=\"/var/tmp/standard.png\" --font-size="+str(fontsize)+" --text-file=\""
        bashcommand+=docpath+"\" "+"\""+testpath+"\""
        print bashcommand
        os.system(str(bashcommand))
        cm = BitmapCompare()
        score = cm.basicCompare("/var/tmp/test.png",\
        "/var/tmp/standard.png")
        return score
