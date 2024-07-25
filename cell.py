from line import Line
from point import Point

class Cell:

    all_corners = ['TL', 'BL', 'TR', 'BR']

    def __init__(self, center_point, walls, window, size):
        self.center_point = center_point
        self.walls = walls
        self.__window = window
        self.__size = size
        self.visited = False

    def get_corners(self, side):
        return list(filter(lambda x: side in x, self.all_corners))

    def get_corner_points(self, corners):
        return list(map(lambda x: self.get_corner_point(x), corners))

    def get_corner_point(self, corner):
        dist_to_corner = self.__size / 2
        match corner:
            case 'TL': return Point(self.center_point.x - dist_to_corner, self.center_point.y - dist_to_corner)
            case 'TR': return Point(self.center_point.x + dist_to_corner, self.center_point.y - dist_to_corner)  
            case 'BL': return Point(self.center_point.x - dist_to_corner, self.center_point.y + dist_to_corner)
            case 'BR': return Point(self.center_point.x + dist_to_corner, self.center_point.y + dist_to_corner)
    
    def draw(self):
        all_walls = ['T', 'L', 'R', 'B']
        for wall in all_walls:
            corner_points = self.get_corner_points(self.get_corners(wall))
            line = Line(corner_points[0], corner_points[1])
            color = "white" if wall in self.walls else "#323232"
            self.__window.draw_line(line, color)

    def draw_move(self, to, undo = False):
        color = "gray" if undo else "red"
        line = Line(self.center_point, to.center_point)
        self.__window.draw_line(line, color)

    def get_facing_border(self, to):
        if self.center_point.x != to.center_point.x and self.center_point.y != to.center_point.y:
            raise Exception("get_facing_border failed due to comparison between non-adjacent cells")
            return
        if self.center_point.x < to.center_point.x: return 'R'
        if self.center_point.x > to.center_point.x: return 'L'
        if self.center_point.y < to.center_point.y: return 'B'
        if self.center_point.y > to.center_point.y: return 'T'
    
