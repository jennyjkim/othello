import tkinter
from othello_model import *



class OthelloBoard:
    def __init__(self, rows: int, columns:int, fplayer: str, corner: str, gamestyle: str):
        self._DEFAULT_FONT = ('courier', 16)
        self._rows = int(rows)
        self._columns = int(columns)
        self._fplayer = ''
        self._corner_piece = ''
        self._gamestyle = ''
        self._winner = ''



        self._black = 0
        self._white = 0
        
        
        if 'B' in fplayer:
            self._fplayer = 'B'
        else:
            self._fplayer = 'W'
            
        if 'B' in corner:
            self._corner_piece = 'B'
        else:
            self._corner_piece = 'W'

        if '>' in gamestyle:
            self._gamestyle = '>'
        else:
            self._gamestyle = '<'
        self._turn = self._fplayer
        
        self._othclass = GameState(self._fplayer, self._gamestyle)
        self._othboard = self._othclass.get_board()

        
        ## CREATE GAME WINDOW
        self._game_window = tkinter.Tk()
        self._game_window.configure(background = 'white')



        ## CREATE CANVAS
        self._canvas = tkinter.Canvas(
            master = self._game_window, width= 600,
            height = 600, background = 'forest green', highlightbackground = 'black')
        self._canvas.grid(
            row = 3, column = 0, rowspan = self._rows, columnspan = self._columns, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S+tkinter.E+tkinter.W)

        self._draw_grid()
        self._set_first_four()
        
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        ## SCORES
        self._scorekeeper()

        ## TURN
        self._turnkeeper()

        ## WINNER
        self._winnerkeeper()
        
        self._game_window.rowconfigure(0, weight = 0)
        self._game_window.rowconfigure(1, weight = 0)
        self._game_window.rowconfigure(2, weight = 0)
        self._game_window.rowconfigure(3, weight = 3)
        self._game_window.columnconfigure(0, weight = 1)

    def start(self) -> None:
        self._game_window.mainloop()

    def _set_scores(self) -> None:
        self._black = self._othclass.get_black()
        self._white = self._othclass.get_white()

    def  _opposite_turn (self):
        if self._turn == 'B':
            return 'W'
        else:
            return 'B'
        
    def _turnkeeper (self) -> None:
        turn_label = tkinter.Label(master = self._game_window, text = 'Turn: '+ self._turn,
                                   font =  self._DEFAULT_FONT, background= 'white')
        turn_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.N+tkinter.S+tkinter.E+tkinter.W)

    def _winnerkeeper(self) -> None:
        self._winner_label = tkinter.Label(master = self._game_window, text = 'WINNER: ' + self._winner,
                                           font = self._DEFAULT_FONT, background = 'white')
        self._winner_label.grid(
            row = 2, column = 0, padx = 10, pady = 0, sticky = tkinter.N+tkinter.S+tkinter.E+tkinter.W)


    def _scorekeeper (self) -> None:
        self._black_score = tkinter.Label(master = self._game_window, text = 'Black: '+ str(self._black),
                                          font = self._DEFAULT_FONT, background = 'white')
        self._black_score.grid(
            row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._white_score = tkinter.Label(master = self._game_window, text = 'White: '+ str(self._white),
                                          font = self._DEFAULT_FONT, background = 'white')
        self._white_score.grid(
            row = 0, column = 0, padx = 10, pady = 10, sticky = tkinter.E)


    def _draw_grid(self) -> None:
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        ## ROWS
        multiplier = (canvas_height / self._rows)
        
        for x in range(self._rows):
            self._canvas.create_line(0, x*multiplier, canvas_width, x * multiplier)

        ## COLUMNS
        multiplier_c = (canvas_width / self._columns)
        
        for y in range(self._columns):
            self._canvas.create_line(y*multiplier_c, 0, y*multiplier_c, canvas_height)

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        self._canvas.delete(tkinter.ALL)
        self._draw_grid()
        self._draw_circle()

    def _set_first_four (self):
        self._othclass.center_four(self._rows, self._columns, self._corner_piece)
        self._othboard = self._othclass.get_board()
        self._set_scores()
        


    def _draw_circle (self) -> None:
        '''Draws a circle for the given othello board coordinate'''
        self._othboard = self._othclass.get_board()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        h_mult = canvas_height / self._rows
        w_mult = canvas_width / self._columns
        
        for row in range(len(self._othboard)):
            for col in range(len(self._othboard[0])):
                if self._othboard[row][col] == 1:
                    self._canvas.create_oval(w_mult*col, h_mult*row, w_mult*(col+1), h_mult*(row+1), fill = 'black')
                if self._othboard[row][col] == 2:
                    self._canvas.create_oval(w_mult*col, h_mult*row, w_mult*(col+1), h_mult*(row+1), fill = 'white')
                    

    def _on_canvas_clicked(self, event: tkinter.Event): 
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        radius_x = canvas_height / (self._rows * 2)
        radius_y = canvas_width / (self._columns * 2)
        
        click_point =(event.x, event.y)
        center_x, center_y = click_point

        click_index = self._which_index(click_point)
        if self._move_possible(click_index) == True:
            self._othclass.make_move(click_index[0], click_index[1])
            self._turn = self._opposite_turn()
            self._turnkeeper()
            self._set_scores()
            self._scorekeeper()
            self._draw_circle()

        if len(self._othclass.all_possible_moves()) == 0:
            self._winner = self._othclass.determine_winner()
            self._winnerkeeper()

        if self._othclass.board_is_full() == True:
            self._winner = self._othclass.determine_winner()
            self._winnerkeeper()
            


    def _which_index (self, click_point: ('x', 'y')) -> ['index']:
        '''Returns the index for where the click was located'''
        index = []
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        h_mult = canvas_height / self._rows
        w_mult = canvas_width / self._columns 

        x_click, y_click = click_point

        for num in range(self._rows):
            if num < 1:
                if y_click < h_mult:
                    index.append(num)
            else:
                if h_mult*num < y_click <= h_mult*(num+1):
                    index.append(num)

        for num1 in range(self._columns):
            if num1 < 1:
                if x_click < w_mult:
                    index.append(num1)
            else:
                if w_mult*num1 < x_click <= w_mult*(num1+1):
                    index.append(num1)
        return index

    def _move_possible (self, index: ['x', 'y']) -> bool:
        '''If the move is within the possible moves, returns TRUE'''
        return index in self._othclass.all_possible_moves()


        
