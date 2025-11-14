import drone_controller
def hay():
	clear()
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			harvest()
			move(East)
		move(North)