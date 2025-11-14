# Funções para movimentação
def goto_x(x):
	n = get_world_size()
	pos = get_pos_x()
	dist_dir = (x - pos) % n 
	dist_esq = (pos - x) % n
	if dist_dir <= dist_esq:
		for _ in range(dist_dir):
			move(East)
	else:
		for _ in range(dist_esq):
			move(West)

def goto_y(y):
	n = get_world_size()
	pos = get_pos_y()
	dist_cim = (y - pos) % n 
	dist_bai = (pos - y) % n
	if dist_cim <= dist_bai:
		for _ in range(dist_cim):
			move(North)
	else:
		for _ in range(dist_bai):
			move(South)
			
def goto(x,y):
	goto_x(x)
	goto_y(y)
	