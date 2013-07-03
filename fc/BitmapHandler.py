from PIL import Image
def white_bg_square(img):
    "return a white-background-color image having the img in exact center"
    size = (max(img.size),)*2
    layer = Image.new('1', size, 1)
    layer.paste(img, tuple(map(lambda x:(x[0]-x[1])/2, zip(size, img.size))))
    return layer

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

class CreateSpriteSheet:
    def __init__(self,pixelsize,font,glyphrange,effects):
        master_width = (pixelsize * (glyphrange[1]-glyphrange[0]+1) )
        #seperate each image with lots of whitespace
        master_height = pixelsize
        print "the master image will by %d by %d" % (master_width, master_height)
        print "creating image..."
        master = Image.new(
        mode='1',
        size=(master_width, master_height),
        color=0) # fully transparent
        print "created."
        fonttype="normal"
        if effects == "italicize":
            font.italicize(-13)
            fonttype="italic"
        count=0;
        for i in range (glyphrange[0],glyphrange[1]):
            location = pixelsize*count
            if effects == "bold":
                font[i].changeWeight(50,"auto",0,0,"auto")
                fonttype = "bold"
            try:
                font[i].export("temp.bmp",pixelsize,1)
                img = Image.open("temp.bmp")
                print "adding %s at %d..." % (str(i)+".bmp", location),
                square_one = white_bg_square(img)
                square_one.resize((sizeo, sizeo))
                master.paste(square_one,(location,0))
                print "added."
            except:
                print "ooopsy"
            count+=1
        print "done adding pics."
        print "saving mastersprite.bmp..."
        master.save('../data/mastersprite'+fonttype+'.bmp' )
        print "saved!"
