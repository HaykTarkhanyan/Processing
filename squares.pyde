
from collections import namedtuple


Line = namedtuple("Line", ["xmin", "xmax"],  rename=False)
# we will need this namedtuple in the class

# for modifing parametrs go to line ~185


class Rectangle:
    """
    Rectangle class has methods to understand which rectangle is nested,
    calculate its area, calculate ovelap area, depending on precentage of overlapped
    area can expand one rectangle or cut it. All this staff is done with taking into
    account that one rectangle is more significant then another one.
    """

    # rectangle is inintialized only by it's cordinates and importance
    def __init__(self, xmin, ymin, xmax, ymax, importance, threshold):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.importance = importance
        self.threshold = threshold
        # we instanciate rectangle to vertical line and horizantal
        self.line_x = Line(self.xmin, self.xmax)
        self.line_y = Line(self.ymin, self.ymax)
        # area of the rectangle
        self.area = self.calculate_area()

    @staticmethod
    def calculate_two_lines_overlap(line_1, line_2):
        # this static method calculates how much two lines overlap
        overlap_size = min(line_1.xmax, line_2.xmax) - \
            max(line_1.xmin, line_2.xmin)
        # we return difference between minimal value of max. cordinates and
        # maximal value of min. cordinates
        if overlap_size < 0:
            return 0
        return min(line_1.xmax, line_2.xmax) - max(line_1.xmin, line_2.xmin)

    @staticmethod
    def check_if_line_nested(line_1, line_2):
        # checks if second line is in first
        if line_2.xmin > line_1.xmin and line_2.xmax < line_1.xmax:
            return True
        # checks if first line is in second
        if line_1.xmin > line_2.xmin and line_1.xmax < line_2.xmax:
            return True

    @staticmethod
    def line_expander(line_1, line_2):
        # functions returns expanded line we will use it in expander function
        return [min(line_1.xmin, line_2.xmin), max(line_1.xmax, line_2.xmax)]

    def line_croper(self, line_1, line_2):
        # functions returns croped line we will use it in croper function
        # assumes that  line_1 is important
        if self.check_if_line_nested(line_1, line_2):
            return "Already Done"
        # checks if less imporant line is from left or right
        if line_2.xmin > line_1.xmin:
            return [line_1.xmax, line_2.xmax]
        else:
            return [line_2.xmin, line_1.xmin]

    def calculate_area(self):
        # fuction calculates area of the rectangle
        return (self.xmax - self.xmin) * (self.ymax - self.ymin)

    def calculate_overlap_area(self, other):
        # uses defined above function once for each axes individually
        return self.calculate_two_lines_overlap(self.line_x, other.line_x) *  \
            self.calculate_two_lines_overlap(self.line_y, other.line_y)

    def check_if_nested(self, other):
        # checks if one rectangle is in another and specifies which one is which
        if self.calculate_overlap_area(other) == self.area:
            return "First is nested in second"
        # it does it by looking which rectangles area is equal to overlap area
        if self.calculate_overlap_area(other) == other.area:
            return "Second is nested in first"
        return 'None of rectangles are nested'

    def cropper(self, other):
        # this function crops less important rectangle to avoid overlaps
        # also minimizes croped area
        if self.line_croper(self.line_x, other.line_x) == "Already Done":
            # if x axes lines are nested we don't change them
            new_min_y, new_max_y = self.line_croper(self.line_y, other.line_y)
            new_min_x, new_max_x = [other.xmin, other.xmax]
            return ("Second rectangle's new cordinates are: \n" +
                    "   xmin, ymin: " + str(new_min_x) + "  " + str(new_min_y) +
                    "\n   xmax, ymax: " +
                    str(new_max_x) + "  " + str(new_max_y),
                    [new_min_x, new_min_y, new_max_x, new_max_y])

        elif self.line_croper(self.line_y, other.line_y) == "Already Done":
            # if y axes lines are nested we don't change them
            new_min_x, new_max_x = self.line_croper(self.line_x, other.line_x)
            new_min_y, new_max_y = [other.ymin, other.ymax]
            return ("First rectangle's new cordinates are: \n" +
                    "   xmin, ymin: " + str(new_min_x) + "  " + str(new_min_y) +
                    "\n   xmax, ymax: " +
                    str(new_max_x) + "  " + str(new_max_y),
                    [new_min_x, new_min_y, new_max_x, new_max_y])

        else:
            # once it changes horizontal cordinates, once vertiacals and compares
            # which crop caused more area to lose
            new_min_x, new_max_x = self.line_croper(
                self.line_x, other.line_x)
            new_min_y, new_max_y = self.line_croper(
                self.line_y, other.line_y)

            # calculating areas in two different cut types
            area_1 = (new_max_x - new_min_x) * \
                     (other.ymax - other.ymin)
            area_2 = (new_max_y - new_min_y) * \
                     (other.xmax - other.xmin)

            if area_1 < area_2:
                # decide which cut is the best
                return ("Second rectangle's new cordinates are: \n" +
                        "   xmin, ymin: " + str(other.xmin) + "  " + str(new_min_y) +
                        "\n   xmax, ymax: " +
                        str(other.xmax) + "  " + str(new_max_y),
                        [other.xmin, new_min_y, other.xmax, new_max_y])
            else:
                return ("Second rectangle's new cordinates are: \n" +
                        "   xmin, ymin: " + str(new_min_x) + "  " + str(other.xmin) +
                        "\n   xmax, ymax: " +
                        str(new_max_x) + "  " + str(other.xmax),
                        [new_min_x, other.xmin, new_max_x, other.xmax])

    def expander(self, other):
        # this functions expands less important rectangle so that imported
        # will become nested in it
        new_min_x, new_max_x = self.line_expander(self.line_x, other.line_x)
        new_min_y, new_max_y = self.line_expander(self.line_y, other.line_y)
        # we update x axes vals and y's seperately
        if self.importance > other.importance:
            other.line_x = Line(new_min_x, new_max_x)
            other.line_y = Line(new_min_y, new_max_y)
            return ("Second rectangle's new cordinates are: \n" +
                    "   xmin, ymin: " + str(new_min_x) + "  " + str(new_min_y) +
                    "\n   xmax, ymax: " +
                    str(new_max_x) + "  " + str(new_max_y),
                    [new_min_x, new_min_y, new_max_x, new_max_y],1)

        # depending of rects importance it changes one of them
        else:
            self.line_x = Line(new_min_x, new_max_x)
            self.line_y = Line(new_min_y, new_max_y)
            return ("First rectangle's new cordinates are: \n" +
                    "   xmin, ymin: " + str(new_min_x) + "  " + str(new_min_y) +
                    "\n   xmax, ymax: " +
                    # added for visualizing
                    str(new_max_x) + "  " + str(new_max_y),
                    [new_min_x, new_min_y, new_max_x, new_max_y],0)

    def case_classifier(self, other):
        # function checks how big is overlaping part and decide to crop or expand
        # also this fucntions runs function coresponding to classified case
        little_rect = min(self.area, other.area)
        overlap_percentage = float(self.calculate_overlap_area(other)) / little_rect
        if overlap_percentage < self.threshold:
            return self.cropper(other)
        return self.expander(other)


def draw_rectangle(rectangle, multiply):
    rect(multiply * rectangle.xmin, multiply * rectangle.ymin, \
         multiply * (rectangle.xmax - rectangle.xmin), \
         multiply * (rectangle.ymax - rectangle.ymin))
    
def draw_boundings(rectangle, multiply):
    line(multiply * rectangle.xmin, multiply * rectangle.ymin, \
         multiply * rectangle.xmax, multiply * rectangle.ymin)
    line(multiply * rectangle.xmin, multiply * rectangle.ymax, \
         multiply * rectangle.xmax, multiply * rectangle.ymax)
    line(multiply * rectangle.xmin, multiply * rectangle.ymin, \
         multiply * rectangle.xmin, multiply * rectangle.ymax)
    line(multiply * rectangle.xmax, multiply * rectangle.ymin, \
         multiply * rectangle.xmax, multiply * rectangle.ymax)




threshold = 0.001
importance_first = 8
importance_second = 6

re_1 = Rectangle(1, 4, 6, 9, importance_first, threshold)
re_2 = Rectangle(4, 6, 9, 8, importance_second, threshold)


def setup():
    size(500, 500)
    threshold = 0.99
    importance_first = 2
    importance_second = 5
    
    global re_1, re_2


def draw():
    global re_1, re_2
    background(220)
    strokeWeight(4)
    draw_boundings(re_1, 50)
    draw_boundings(re_2, 50)
    
    if re_1.importance > re_2.importance:
        fill(0,255,255)
        draw_rectangle(re_1, 50)
        fill(255,0,255)
        draw_rectangle(re_2, 50)
    else:
        fill(255,0,255)
        draw_rectangle(re_2, 50)
        fill(0,255,255)
        draw_rectangle(re_1, 50)
        
    draw_boundings(re_1, 50)
    draw_boundings(re_2, 50)

    if keyPressed:
        if keyCode == LEFT:
            a = re_1.case_classifier(re_2)
            print (a)
            fill ( 255, 0, 0)
            if not a[2]:
                # re_1 = 
                re_2.xmin, re_2.ymin, re_2.xmax, re_2.ymax = a[1]
            else:
                re_1.xmin, re_1.ymin, re_1.xmax, re_1.ymax = a[1]
        if keyCode == RIGHT:
            pass
            # re_1.xmin, re_1.ymin, re_1.xmax, re_1.xmax = old_re_1_xmin, old_re_1_ymin, old_re_1_xmax, old_re_1_xmax
            # re_2.xmin, re_2.ymin, re_2.xmax, re_2.xmax = old_re_2_xmin, old_re_2_ymin, old_re_2_xmax, old_re_2_xmax  
        # noLoop()
        
        
# print (vars(re_2))
