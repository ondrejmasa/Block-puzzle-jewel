class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    pink = (255, 51, 153)
    menthol = (0, 255, 128)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.menthol, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue, cls.pink, cls.menthol, cls.orange, cls.yellow, cls.blue, cls.purple, cls.pink]


small_cell_size = 33
cell_size = 50

small_startpoint_x = 13
small_startpoint_y = 421
startpoint_x = startpoint_y = 11
