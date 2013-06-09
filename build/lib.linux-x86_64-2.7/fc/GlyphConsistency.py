class GlyphConsistency:
    #computes the number of selfIntersects in the glyph is any across
    #all layers, it is a self consistency check
    def glyph_selfIntersects(self, glyph):
        count=0
        score=0
        for layer in glyph.layers:
            if layer.selfIntersects():
                score+=1
            count+=1
        return self.output(score,total)
