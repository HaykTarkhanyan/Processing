class Board:
    def __init__(self, bg_color, line_color):
        # we initialize bord by background color and 
        # grid lines color
        self.bg_color = bg_color
        self.line_color = line_color
        
    def display(self):
        background(self.bg_color)
        for i in range(1,3):
            # makes 3x3 grid 
            stroke(self.line_color)
            line(width/3 * i, 0, width/3 * i, height)
            line(0 , height/3 * i, width, height/3 * i)
