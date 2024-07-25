from tkinter import Tk, BOTH, Canvas
from line import Line
from point import Point
from cell import Cell
from maze import Maze

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Test"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)





def main():
    win = Window(800, 600)
    maze = Maze(win, 5, 5, 10, 25)
    maze._break_exits()
    maze._break_walls_r(0,0)
    maze._reset_visited_cells()
    maze.solve()
    # test_cell = Cell(Point(100, 100), ['L','T','R'], win, 30)
    # test_cell2 = Cell(Point(100, 130), ['L', 'B'], win, 30)
    # test_cell.draw()
    # test_cell2.draw()
    # test_cell.draw_move(test_cell2)
    win.wait_for_close()

if __name__ == '__main__':
    main()
