import unittest
from maze import Maze
from cell import Cell
from point import Point

class Test(unittest.TestCase):
    def test_maze_size(self):
        m = Maze(None, 5, 10, 5, 5)
        self.assertEqual(len(m._cells), 5)
        self.assertEqual(len(m._cells[0]), 10)

    def test_cell_placement(self):
        m = Maze(None, 3, 3, 10, 10)
        self.assertEqual(m._cells[2][2].center_point.x, 35)

    def test_entrance_and_exit(self):
        m = Maze(None, 3, 3, 10, 10)
        m._break_exits()
        self.assertEqual('T' not in m._cells[0][0].walls, True)
        self.assertEqual('B' not in m._cells[2][2].walls, True)

    def test_cell_reset(self):
        m = Maze(None, 3, 3, 10, 10)
        m._break_walls_r(0,0)
        m._reset_visited_cells()
        for x in range(0, m._rows):
            for y in range(0, m._columns):
                self.assertEqual(m._cells[x][y].visited, False)

if __name__== "__main__":
    unittest.main()
