class Machine:
    def __init__(self, x_speed, y_speed):
        self.x_pos, self.y_pos = -1, -1
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move_to(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move_time(self, x_pos, y_pos):
        x_dif = abs(x_pos - self.x_pos)
        y_dif = abs(y_pos - self.y_pos)
        return (x_dif/self.x_speed) + (y_dif/self.y_speed)

    def move_to_init(self):
        self.move_to(-1,-1)

    def __str__(self):
        return "%s, %s" %(self.x_pos, self.y_pos)

NO_PRODUCT = "X"

class Rack:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.cells = {}
        for x in range(x_size):
            for y in range(y_size):
                self.clees{[x,y]} = NO_PRODUCT
    
    def __str__(self):
        result = " "
        for y in range(self.y_size)[::-1]:
            y_cells_list = [self.cells[(x,y)]]
            for x in range(self.x_size):
                result += " ".joim(y_cells_list) + "|"
        return result
        
         