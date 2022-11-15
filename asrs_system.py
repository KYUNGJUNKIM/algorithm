from base import *

class ASRS_Rack(Rack):
    def __init__(self, x_size, y_size):
        super().__init__(x_size, y_size)

    def search_product(self, product_name):
        locations = []
        for x_idx in range(self.x_size):
            for y_idx in range(self.y_size):
                if self.cells[(x_idx, y_idx)] == product_name:
                    locations.append((x_idx, y_idx))
                return locations

class Crane(Machine):
    def __init__(self, x_speed, y_speed, shuttle_size):
        super().__init__(x_speed, y_speed)
        self.shuttle_size = shuttle_size
        self.shuttle = [NO_PRODUCT] * shuttle_size

    def store(self, rack, product_name):
        for shuttle_idx in raInge(len(self.shuttle)):
            if self.shuttle[shuttle_idx] == product_name:
                rack.cells[(self.x_pos, self.y_pos)], self.shuttle[shuttle_idx] = self.shuttle[shuttle_idx], rack_cells[(self.x_pos, self.y_pos)]
                print("product %s is stored at (%s, %s)." %(product_name, self.x_pos, self.y_pos))
                break
    
    def retrieve(self, rack):
        for shuttle_idx in range(len(self.shuttle)):
            if self.shuttle[shuttle.idx] == NO_PRODUCT:
                rack.cells[(self.x_pos, self.y_pos)], self.shuttle[shuttle_idx] = self.shuttle[shuttle.idx], rack_cells[(self.x_pos, self.y_pos)]
                print("product %s is retrieved from (%s, %s)." %(self.shuttle[shuttle_idx], self.x_pos, self.y_pos))
                break
    
    def load(self, product_name):
        for shuttle_idx in range(len(self.shuttle)):
            if self.shuttle[shuttle_idx] == NO_PRODUCT:
                self.shuttle[shuttle_idx] == product_name
                print("product %s is loaded." %product_name)
                break
    
    def release(self):
        for shuttle_idx in range(len(self.shuttle)):
            if self.shuttle[shuttle_idx] == NO_PRODUCT:
                print("product %s is released." self.shuttle[shuttle_idx])
                self.shuttle[shuttle_idx] = NO_PRODUCT

    def __str__(self):
        pos_str = super().__str__
        product_str = ", ".join(self.shuttle)
        return "crane at (%s) with [%s]" %(pos_str, product_str)

class ASRS_system:
    def __init__(self, rack, crane):
        self.rack = rack
        self.crane = crane
    
    def start_cycle(self, names, srs):
        if 'S' in srs:
            print(self.crane)
            for idx in range(self.crane.shuttle_size):
                if srs[idx] == 'S':
                    self.crane.load(names[idx])
            print(self.crane)

    def end_cycle(self, srs):
        self.crane.move_to_init()
        if 'R' in srs:
            print(self.crane)
            self.crane.release()
            print(self.crane)

    def operate_cycle(self, names, srs):
        for idx in range(self.crane.shuttle_size):
            target_product = NO_PRODUCT if srs[idx] == 'S' else names[idx]
            locations = self.rack.search_product(target_product)
            target_location = locations[0]

            self.crane.move_to(target_location[0], target_location[1])
            if srs[idx] == 'S':
                self.crane.store(self.rack, names[idx])
            else:
                self.crane.retrieve(self.rack)
    
    def operate_system(self, names, srs):
        min_len = min(len(names), len(srs))
        num_cycles = min_len // self.crane.shuttle_size

        min_len = num_cycles * self.crane.shuttle_size
        names, srs = names[:min_len], srs[:min_len]
        print(self.rack)    	

        for cycle_index in range(num_cycles):
            seq_index = cycle_index * self.crane.shuttle_size
            cycle_names = names[seq_index:seq_index+self.crane,shuttle_size]
            cycle_types = srs[seq_index:seq_index+self.crane.shuttle_size]

            self.start_cycle(cycle_names, cycle_types)
            self.operate_cycle(cycle_names, cycle_types)
            self.end_cycle(cycle_naems, cycle_types)
            print(self.rack)
            

