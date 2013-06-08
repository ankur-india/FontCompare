from PIL import Image

class BitmapCompare:
    def basicCompare(self,testbmp,standardbmp):
        test = Image.open(testbmp)
        standard = Image.open(standardbmp)
        width, height = standard.size
        width2, height2=test.size
        width = min(width,width2)
        height = min(height, height2)
        test = test.load()
        standard = standard.load()
        count=0
        i=0
        while i<height:
            j = 0  
            while j<width:
                if j<width2 and i<height2 :
                    if test[j,i]== standard[j,i]:
                        count+=1
                j = j+1
            i = i+1
        return (float(count)/float(height*width))*100
