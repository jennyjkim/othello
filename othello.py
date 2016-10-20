# Jisoo Kim ID 72238150. Project 5.
# othello_gui

import tkinter
from othello_game_board import *



class OthelloStartup:
    def __init__ (self):
        self._DEFAULT_FONT = ('courier', 16)
        self._rows = 0
        self._columns = 0
        self._fplayer = ''
        self._corner_piece = ''
        self._gamestyle = ''
        
        # create root window
        self._root_window = tkinter.Tk()
        self._root_window.geometry('750x650')
        self._root_window.configure(background = 'forest green')
        
        # welcome label
        self._welcome_label = tkinter.Label(
            master = self._root_window, text = 'Welcome to Othello!',
            font = ('courier', 28), fg = 'white', relief = 'ridge', background = 'forest green')

        self._welcome_label.grid(row = 0, column = 0, padx = 20, pady = 20,
                           sticky = tkinter.S)

        # 'Please select desired Othello game options: ' LABEL
        self._header_label = tkinter.Label(
            master = self._root_window,
            text = 'Please select desired Othello game options :',
            font = ('Courier', 20), background = 'forest green')

        self._header_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                          sticky = tkinter.N)

        # Drop down -- ROWS -- menu
        self._row_label = tkinter.Label(master = self._root_window,
                                        text = 'How many rows?', font = self._DEFAULT_FONT,
                                        background = 'forest green')
        self._row_label.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        
        self._variable = tkinter.StringVar(self._root_window)
        self._variable.set(4)
        self._drop_down_rows = tkinter.OptionMenu(self._root_window, self._variable,
                                            4, 6, 8, 10, 12, 14, 16)
        self._drop_down_rows.config(bg = 'forest green')
    
        self._drop_down_rows.grid(
            row = 2, column = 0, padx = 10, pady = 10)
        
        # Drop down -- COLUMNS -- menu
        self._column_label = tkinter.Label(master = self._root_window,
                                           text = 'How many columns?', font = self._DEFAULT_FONT,
                                           background = 'forest green')
        self._column_label.grid(row = 3, column = 0, padx = 10, pady = 10,sticky = tkinter.W)
        self._variable1 = tkinter.StringVar(self._root_window)
        self._variable1.set(4)
        self._drop_down_columns = tkinter.OptionMenu(self._root_window, self._variable1,
                                            4, 6, 8, 10, 12, 14, 16)
        self._drop_down_columns.config(bg = 'forest green')
        
        self._drop_down_columns.grid(
            row = 3, column = 0, padx = 10, pady = 10)

        # Drop down -- FIRST PLAYER -- menu
        self._column_label = tkinter.Label(master= self._root_window, text = 'First player?',
                                           font = self._DEFAULT_FONT, background = 'forest green')
        self._column_label.grid(
            row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._variable2 = tkinter.StringVar(self._root_window)
        self._variable2.set('Black (B)')
        self._drop_down_player = tkinter.OptionMenu(self._root_window, self._variable2,
                                            'Black (B)', 'White (W)')
        self._drop_down_player.config(bg = 'forest green')                                          
        self._drop_down_player.grid(
            row = 4, column = 0, padx = 10, pady = 10)
        
        # Drop down -- TOP-LEFT CORNER PIECE -- menu
        self._corner_header = tkinter.Label(master = self._root_window,
                                            text = 'Top-left corner piece?', font = self._DEFAULT_FONT,
                                            background = 'forest green')
        self._corner_header.grid(
            row = 5, column = 0, padx= 10, pady=10, sticky = tkinter.W)
        self._variable3 = tkinter.StringVar(self._root_window)
        self._variable3.set('Black (B)')
        self._drop_down_corner = tkinter.OptionMenu(self._root_window, self._variable3,
                                            'Black (B)', 'White (W)')
        self._drop_down_corner.config(bg = 'forest green')                                        
        self._drop_down_corner.grid(
            row = 5, column = 0, padx = 10, pady = 10)
        
        # Drop down -- GAME STYLE -- menu
        self._style_header = tkinter.Label(master = self._root_window, text = 'Gamestyle?',
                                           font = self._DEFAULT_FONT, background = 'forest green')
        self._style_header.grid(
            row = 6, column = 0, padx = 10, pady = 10, sticky = tkinter.W)
        self._variable4 = tkinter.StringVar(self._root_window)
        self._variable4.set('Greatest # of pieces win (>)')
        self._drop_down_gamestyle = tkinter.OptionMenu(self._root_window, self._variable4,
                                                 'Greatest # of pieces wins (>)',
                                                 'Least # of pieces wins (<)')
        self._drop_down_gamestyle.config(bg = 'forest green')
        self._drop_down_gamestyle.grid(
            row = 6, column = 0, padx = 10, pady = 10)

        # Button - OK
        self._button_ok = tkinter.Button(
            master = self._root_window, text = 'Play Othello!',
            font = ('Courier', 16), highlightbackground = 'forest green',
            command = self._on_ok_clicked)
        self._button_ok.grid(
            row = 7, column = 0, padx = 10, pady = 20, sticky = tkinter.N)
            

        self._root_window.rowconfigure(0, weight = 2)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.rowconfigure(5, weight = 1)
        self._root_window.rowconfigure(6, weight = 1)
        self._root_window.rowconfigure(7, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        
    def start(self) -> None:
        self._root_window.mainloop()

    def _on_ok_clicked(self) -> None:
        self._rows = self._variable.get()
        self._columns = self._variable1.get()
        self._fplayer = self._variable2.get()
        self._corner_piece = self._variable3.get()
        self._gamestyle = self._variable4.get()

        self._root_window.destroy()
        game = OthelloBoard(self._rows, self._columns, self._fplayer, self._corner_piece, self._gamestyle)
        game.start()


       

if __name__ == '__main__':
    OthelloStartup().start()

