import drone_controller

import globals

def carrot():
	cost = get_cost(Entities.Carrot)
	for key in cost:
		required = cost[key] * 10000
		while num_items(key) < required:
			globals.functions[key]()  
	drone_controller.goto(0, 0)
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type()!=Grounds.Soil:
				till()
				plant(Entities.Carrot)
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			move(East)
		move(North)
			