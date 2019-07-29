class Board:
    def __init__(self, bg_color, line_color):
        self.bg_color = bg_color
        self.line_color = line_color
        
    def display(self):
        background(self.bg_color)
        for i in range(1,3):
            stroke(self.line_color)
            line(width/3 * i, 0, width/3 * i, height)
            line(0 , height/3 * i, width, height/3 * i)
