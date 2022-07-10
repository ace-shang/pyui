

class Color():
    fWrite_bCyan = 1
    def __init__(self, crs):
        self.crs = crs
        crs.start_color()
        crs.init_pair(self.fWrite_bCyan, crs.COLOR_WHITE, crs.COLOR_CYAN)

    def get_pair(self, num):
        return self.crs.color_pair(num)

