
class Colors:
	dark_grey = (255, 255, 255)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (255, 255, 255)
	light_blue = (200, 100, 150) 
	pink = (255, 192, 203)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
