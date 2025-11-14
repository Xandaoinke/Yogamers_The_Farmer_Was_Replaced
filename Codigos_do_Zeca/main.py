import hay, wood, carrot, pumpkin, cactus, globals

globals.functions = {
	Items.Hay: hay.hay,
	Items.Wood: wood.wood,
	Items.Carrot: carrot.carrot,
	Items.Pumpkin: pumpkin.pumpkin,
	Items.Cactus: cactus.cactus
}

objectives = [Unlocks.Carrots, Unlocks.Pumpkins, Unlocks.Cactus, Unlocks.Mazes, Unlocks.Dinosaurs]
for objective in objectives:
	
	cost = get_cost(objective)
	
	def can_afford(cost):
		for key in cost:
			if num_items(key) < cost[key]:
				return False
		return True
	
	clear()
	
	while not can_afford(cost):
		for key in cost:
			if num_items(key) < cost[key]:
				globals.functions[key]()
				break
				
	unlock(objective)
	