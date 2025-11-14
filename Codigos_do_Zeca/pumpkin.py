import drone_controller
import globals

def pumpkin():
	cost = get_cost(Entities.Pumpkin)
	for key in cost:
		required = cost[key] * 10000
		while num_items(key) < required:
			globals.functions[key]()  
	drone_controller.goto(0, 0)
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type()!=Grounds.Soil:
				till()
			plant(Entities.Pumpkin)
			move(East)
		move(North)
	clean=False
	while not clean:
		clean = True
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				if get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
					clean = False
				move(East)
			move(North)
	harvest()