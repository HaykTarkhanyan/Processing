import initial_board
import elements
import additional

X_TURN = True
# because I can't use more convenient way to initialize 
# empty board N will stand for None and I will change some N's to 
# corresponding new value (X or O)
BOARD = [["N", "N", "N"],
         ["N", "N", "N"],
         ["N", "N", "N"]]
         
def mouseClicked():
    # fucntion is for making moves
    # x_turn helps understand what to add o or x    
    global X_TURN
    global BOARD
    
    # mouse cordinates are converted to grid location(e.g.[0,2])
    positions = additional.understand_cell([mouseX, mouseY])
    # we add element only if cell is empty
    if  X_TURN and BOARD[positions[0]][positions[1]] == "N":
        X_TURN = False
        x.append(elements.X(positions))  
        BOARD[positions[0]][positions[1]] = "X"
        
    elif BOARD[positions[0]][positions[1]] == "N":
        X_TURN = True
        o.append(elements.O(positions))
        BOARD[positions[0]][positions[1]] = "O"

def setup():
    size(700,700)
    board = initial_board.Board('#a2b3c4', '#ffff00')
    board.display()
    global x, o
    x = []
    o = []
    
def draw():
    
    for i in range(len(x)):
        x[i].display()
    for i in range(len(o)):
        o[i].display()
            
    print (BOARD)
