# board size for computer

def setup():
  size(560,680) 
  frameRate(9)
  direc = 'UP'
  firstx = 40 * int(random(width/40))
  firsty = 40 * int(random(height/40))
  global score
  
  score = 0
  
  global snake
  global food
  snake = [Snake(40, firstx, firsty, 'nothing')]
# snake_test = Snake(40,400,120)
  food = Food()

 


def draw():
  background(255,255,255)
  global score
  for i in range(width/40):
    line(40*i, 0, 40*i, height)
  for i in range(height/40):
    line(0, 40*i, width, 40*i)

  for i in range(len(snake)):
    snake[i].move()
    snake[i].display()
    snake[i].die()
    food.display()
    perfect_play()

    fill(0,255,0)
    textSize(150)
    textAlign(CENTER)
  
    text(score, 5*width/7, height/4)
    
    if snake[0].xpos == food.xfood and snake[0].ypos == food.yfood:
      make_food()
      score += 1
        
         
        




class Snake ():
   def __init__ (self, box_size, xpos, ypos, direction):
     self.box_size = box_size
     self.xpos = xpos
     self.ypos = ypos
     self.direction = direction
     self.xspeed = 0
     self.yspeed = 0
     
   def display(self):
     fill(0,255,255)
     self.xpos += self.xspeed
     self.ypos += self.yspeed
     rect(self.xpos, self.ypos, self.box_size, self.box_size)

   def move(self):
       if keyPressed:
          if keyCode == LEFT or key == 'a' or key == 'A':
             self.direction = 'LEFT'
             # self.xspeed = -self.box_size
             # self.yspeed = 0
          elif keyCode == RIGHT or  key == 'd' or key == 'D':
             self.direction = 'RIGHT' 
             # self.xspeed = self.box_size
             # self.yspeed = 0
          elif keyCode == UP or key == 'w' or key == 'W':
             self.direction = 'UP'
             # self.yspeed = -self.box_size
             # self.xspeed = 0
          elif keyCode == DOWN or key ==  's' or key == 'S':
             self.direction = 'DOWN'
             # self.yspeed = self.box_size
             # self.xspeed = 0
             
       if self.direction == "LEFT":
           self.xspeed = -self.box_size
           self.yspeed = 0
       elif self.direction == "RIGHT":
           self.xspeed = self.box_size
           self.yspeed = 0
       elif self.direction == "UP":
           self.yspeed = -self.box_size
           self.xspeed = 0
       elif self.direction == "DOWN":
           self.yspeed = self.box_size
           self.xspeed = 0
   
   
   
   
   def die(self):
       if self.xpos == -self.box_size or self.xpos == width \
       or self.ypos == -self.box_size or self.ypos == height:
           fill(255,0,255)
           textSize(80)
           text('GAME OVER', width/2,height/2)
           noLoop()         
  
   
   
class Food():
    def __init__ (self):
        self.xfood = snake[0].box_size * int(random(width/snake[0].box_size))
        self.yfood = snake[0].box_size * int(random(height/snake[0].box_size))
    def display(self):
        fill(255,0,0)
        rect(self.xfood, self.yfood, snake[0].box_size, snake[0].box_size) 
        
        
def make_food():
    old_x = food.xfood 
    old_y = food.yfood   
    rand_x =  snake[0].box_size * int(random(width/snake[0].box_size))
    rand_y =  snake[0].box_size * int(random(width/snake[0].box_size))
    
    for i in range(len(snake)):
        if rand_x == snake[i].xpos and rand_y == snake[i].ypos:
                 make_food()
    else:
      print ('unicorn')
      food.xfood = rand_x
      food.yfood = rand_y
      for i in range(len(snake)):
        if food.xfood != snake[i].xpos or food.yfood != snake[i].ypos:
          print ('rainbow')
          # noLoop()
          snake.append(Snake(40, old_x, old_y, snake[0].direction))
    
