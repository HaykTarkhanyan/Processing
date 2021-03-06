global X_COLOR, O_COLOR

# just colors for displaying pieces
X_COLOR = '#ac1234'
O_COLOR = '#140EEA'

class X:    
    def __init__(self, cell_cord):    # cell_cord[0] - # of row
        self.cell_cord = cell_cord    # cell_cord[1] - # of column
        
    def display(self):   # beacause we always deal with square \
                         # boards i will use only width even when its not logical
        noFill()
        strokeWeight(4)
        stroke(X_COLOR)
        space = width / 30 # distance from edge    
        # simple algorithm for drowing crossing lines
        line(space + self.cell_cord[1] * width / 3 , space + self.cell_cord[0] * width/3 , \
             (self.cell_cord[1]+1) * width / 3 - space, (self.cell_cord[0] + 1) * width/3 - space)
        line((self.cell_cord[1]+1) * width /3 - space, space + self.cell_cord[0] * width/3, \
             space + self.cell_cord[1] * width / 3 , (self.cell_cord[0] + 1) * width/3 - space) 

class O(X):
    # because O and X have a lot in common we inherit and only override
    # function for displaying
    def __init__(self,  cell_cord):
        self.cell_cord = cell_cord
        
    def display(self):
        space = width / 30 # distance from edge
        noFill()
        stroke(O_COLOR)    
    
        circle(width / 3 / 2 + self.cell_cord[1] * width/3, width / 3 / 2 + self.cell_cord[0] * width/3,  \
               width / 3 - space) 
