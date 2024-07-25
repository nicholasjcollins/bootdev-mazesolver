from cell import Cell
from point import Point
import time
import random

class Maze:

    directions = {"T":(-1, 0), "B":(1,0), "L":(0, -1), "R":(0,1)}

    def __init__(self, win, rows, columns, tl_padding, cell_size):
        self._win = win
        self._rows = rows
        self._columns = columns
        self._tl_padding = tl_padding
        self._cell_size = cell_size
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for x in range(0, self._rows):
            self._cells.append([])
            for y in range(0, self._columns):

                center_point = Point(
                    (self._tl_padding - self._cell_size /2)  + self._cell_size * (y + 1),
                    (self._tl_padding - self._cell_size / 2) + self._cell_size * (x + 1))
                    # (self._tl_padding - self._cell_size /2)  + self._cell_size * (y + 1))
                cell = Cell(center_point, ['L','R','T','B'], self._win, self._cell_size)
                self._cells[x].append(cell)
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        if self._win == None: return
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.25)

    def _break_exits(self):
        if len(self._cells) == 0: return
        top_left = self._cells[0][0]
        bottom_right = self._cells[self._rows - 1][self._columns - 1]
        if 'T' in top_left.walls: 
            top_left.walls.remove('T')
            self._draw_cell(top_left)

        if 'B' in bottom_right.walls: 
            bottom_right.walls.remove('B')
            self._draw_cell(bottom_right)
       
    def _break_walls_r(self, x, y):
        cell = self._cells[x][y]
        cell.visited = True
        while True:
            print("Entered break_walls_r loop")
            potential = []
            for d in self.directions:
                ax = x + self.directions[d][0]
                ay = y + self.directions[d][1]
           # for ax in range(x - 1, x + 2):
            #    for ay in range(y -1, y + 2):
             #   if ax == x and ay == y: continue
             #   if ax != x and ay != y: continue
                if ax < 0 or ax >= self._rows: continue
                if ay < 0 or ay >= self._columns: continue
                ac = self._cells[ax][ay]
                if not ac.visited:
                    potential.append((ac, ax, ay))
            if len(potential) == 0:
                self._draw_cell(cell)
                return
            target = potential[random.randrange(0, len(potential))]
            target_cell = target[0]
            cell_border = cell.get_facing_border(target_cell)
            target_border = target_cell.get_facing_border(cell)
            cell.walls.remove(cell_border)
            target_cell.walls.remove(target_border)
            self._draw_cell(cell)
            self._draw_cell(target_cell)
            self._break_walls_r(target[1], target[2])

    def _reset_visited_cells(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False


    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, x, y):
        self._animate()
        current_cell = self._cells[x][y]
        current_cell.visited = True
        if x == self._rows - 1 and y == self._columns - 1: return True
        for d in self.directions:
            ax = x + self.directions[d][0]
            ay = y + self.directions[d][1]
            if ax < 0 or ax >= self._rows: continue
            if ay < 0 or ay >= self._columns: continue
            if d in current_cell.walls: continue
            ac = self._cells[ax][ay]
            print(f"found valid path in direction {d} from cell {current_cell.center_point.x},{current_cell.center_point.y} to cell {ac.center_point.x},{ac.center_point.y}")
            if ac.visited: continue
            current_cell.draw_move(ac)
            if self._solve_r(ax, ay): return True
            current_cell.draw_move(ac, True)
        return False

            
            
        


        

            

