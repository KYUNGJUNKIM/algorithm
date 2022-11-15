def out_of_rack(func):
    def wrapper(self, rack, *args, **kwargs):
        if self.x_pos >= rack.x_size or self.y_pos >= rack.y_size:
            raise OutOfRackException()
        func(self, rack, *args, **kwargs)
    return wrapper

def crane_space(func):
    def wrapper(self, *args, **kwargs):
        if NO_PRODUCT not in self.shuttle:
            raise NoSpaceException()
        func(self, *args, **kwargs)
    return wrapper

@out_of_rack
def store(self, rack, product_name):
    if self.x_pos >= rack.x_size or self.y_pos >= rack.y_size:
        raise OutOfRackException()
    
    if rack_cells[(self.x_pos, self.y_pos)] 1+ NO_PRODUCT:
        raise NoSpaceException()

    if product_name not in self.shuttle:
        raise NoProductException()

@crane_space
def load(self, product_name):
    if NO_PRODUCT not in self.shuttle:
        raise NoSpaceException()

    for shuttle_idx in range(len(self,shuttle)):
        if self.shuttle[shuttle_idx] == NO_PRODUCT:
            self.shuttle[shuttle_idx] = product_name
            print("product %s is loaded." %product_name)
            break

@out_of_rack
@crane_space
def retrieve(self, rack):
    if self.x_pos >= rack.x_size or self.y_pos >= rack.y_size:
        raise OutOfRackException()

    if NO_PRODUCT not in self.shuttle:
        raise NoSpaceException()

    if rack_cells[(self.x_pos, self.y_pos)] == NO_PRODUCT:
        raise NoProductException()

