import drone_controller
import globals

def cactus():
	cost = get_cost(Entities.Cactus)
	for key in cost:
		required = cost[key] * 10000
		while num_items(key) < required:
			globals.functions[key]()  
	drone_controller.goto(0, 0)
	for _ in range(get_world_size()):
		plant_cactus()
		order_cactus_x()
		move(North)
	for _ in range(get_world_size()):
		order_cactus_y()
		move(East)
	drone_controller.goto(0,0)
	harvest()

def order_cactus_x():
	for i in range(1, get_world_size()):
		drone_controller.goto_x(i)
		key_i = measure()
		j = i - 1
		while j >= 0:
			drone_controller.goto_x(j)
			key_j = measure()
			if key_j > key_i:
				swap(East)
				j-=1
			else:
				break
	drone_controller.goto_x(0)
	
def order_cactus_y():
	for i in range(1, get_world_size()):
		drone_controller.goto_y(i)
		key_i = measure()
		j = i - 1
		while j >= 0:
			drone_controller.goto_y(j)
			key_j = measure()
			if key_j > key_i:
				swap(North)
				j-=1
			else:
				break
	drone_controller.goto_y(0)
	
def plant_cactus():
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		move(East)