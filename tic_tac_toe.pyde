import initial_board
import elements
import additional

def setup():
    size(700,700)
    board = initial_board.Board('#a2b3c4', '#ffff00')
    board.display()
    global x, o
    x = []
    o =[]

    counter = 0    
def draw():
    
    board = initial_board.Board('#a2b3c4', '#ffff00')

    print (counter)
    if mousePressed:
        
        if  counter %2 == 0:
            counter += 1
            X_TURN = False
            x.append(elements.X(additional.understand_cell([mouseX, mouseY])))           
        else:
            X_TURN = True
            o.append(elements.O(additional.understand_cell([mouseX, mouseY])))
        counter += 1
    print (o)
    for i in range(len(x)):
            x[i].display()
    for i in range(len(o)):
            o[i].display()
        
