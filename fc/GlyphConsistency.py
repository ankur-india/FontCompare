from fc.BitmapCompare import BitmapCompare
class GlyphConsistency:
    #computes the number of selfIntersects in the glyph is any across
    #all layers, it is a self consistency check
    def glyph_basicConsistency(self, glyph):
        #worth outputting
        if glyph.isWorthOutputting():
            scoreFactor = 1
        else:
            scoreFactor = 0
        #no counter intersection
        count=0
        score=0
        for layer in glyph.layers:
            if layer.selfIntersects():
                score+=1
            count+=1
        return (score/count)*scoreFactor

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
                    xmin_cords.append(font[i].boundingBox()[1])
                if not font[i].boundingBox()[2] in xmax_cords:
                    xmin_cords.append(font[i].boundingBox()[2])
                if not font[i].boundingBox()[3] in xmin_cords:
                    xmin_cords.append(font[i].boundingBox()[3])
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
                    if font[i].script is script:
                        set_script_score+=1
                    font[i].export("before.bmp",50,1)
                    font[i].round()
                    font[i].export("after.bmp",50,1)
                    score =  bitcomp.basicCompare("before.bmp","after.bmp")
                    if score is 100:
                        set_round_score+=1
                    total+=1
            set_round_score = set_round_score/float(total)
            return set_round_score

