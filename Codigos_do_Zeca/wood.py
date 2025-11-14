import drone_controller
def wood():
	drone_controller.goto(0,0)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type()!=Grounds.Grassland:
				till()
			if (j+i)%2!=0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(East)
		move(North)