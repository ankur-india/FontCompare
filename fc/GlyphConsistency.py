from fc.BitmapHandler import BitmapCompare
class GlyphConsistency:
    #computes the number of selfIntersects in the glyph is any across
    #all layers, it is a self consistency check
    def glyph_basicConsistency(self, font, range_tuple):
        scores = list()
        total = 0
        for i in range (range_tuple[0],range_tuple[1]):
            #worth outputting
            try:
                if font[i].isWorthOutputting():
                    scoreFactor = 1
                else:
                    scoreFactor = 0
            except:
                scoreFactor = 0
            #no counter intersection
            score=10
            if font[i].layers[1].selfIntersects():
                score=0
            total+=score
            scores.append((font[i].glyphname,score*scoreFactor))
        scores.append(("Basic Consistency Score: ",total/len(scores)))
        return scores

    def glyph_basicset_consistency(self, font, range_tuple):
        total = 0
        #bbox consistency
        xmin_cords = list()
        ymin_cords = list()
        ymax_cords = list() 
        xmax_cords = list()
        #bearing consistency 
        lbearing = list()
        rbearing = list()
        #layer count consistency
        layer_cnts = list()
        for i in range (range_tuple[0],range_tuple[1]):
            if i in font:
                if not font[i].boundingBox()[0] in xmin_cords:
                    xmin_cords.append(font[i].boundingBox()[0])
                if not font[i].boundingBox()[1] in ymin_cords:
                    ymin_cords.append(font[i].boundingBox()[1])
                if not font[i].boundingBox()[2] in xmax_cords:
                    xmax_cords.append(font[i].boundingBox()[2])
                if not font[i].boundingBox()[3] in ymax_cords:
                    ymax_cords.append(font[i].boundingBox()[3])
                if not font[i].left_side_bearing in lbearing:
                    rbearing.append(font[i].left_side_bearing)
                if not font[i].right_side_bearing in rbearing:
                    rbearing.append(font[i].right_side_bearing)
                if not font[i].layer_cnt in layer_cnts:
                    layer_cnts.append(font[i].layer_cnt)
            total+=1
        count=len(xmin_cords)+len(xmax_cords)+len(ymin_cords)+len(ymax_cords)
        count = count+ len(rbearing) + len(lbearing) + len(layer_cnts)
        set_basic_score = count/float(total*7)
        return set_basic_score*10

    def glyph_round_consistency(self, font, range_tuple):
        #script and rounding consistency
        bitcomp = BitmapCompare()
        set_round_score=0
        total=0
        net_score = list()
        for i in range (range_tuple[0],range_tuple[1]):
            if i in font:
                font[i].export("/var/tmp/before.bmp",50,1)
                font[i].round()
                font[i].export("/var/tmp/after.bmp",50,1)
                score =  bitcomp.basicCompare("/var/tmp/before.bmp", \
                "/var/tmp/after.bmp")
                if score == 100.0:
                    set_round_score+=1
                total+=1
        return (set_round_score/float(total))*10

