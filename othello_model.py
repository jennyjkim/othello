# Jisoo (Jenny) Kim ID: 72238150 PROJECT 5
# othello_model
    
########## CLASS ##########


class GameState:
    def __init__ (self, turn: str, style: str):
        self._board = []
        self._black = 0
        self._white = 0
        self._turn = turn
        self._gamestyle = style

        self._NONE = 0
        self._BLACK = 1
        self._WHITE = 2


    def center_four(self, rw: int, col: int, start_color: str):
        board = create_board(rw, col)
        if start_color == 'B':
            for x in range(len(board)):
                x1 = x + 1
                if x1 == rw/2:
                    board[x][int(col/2)] = self._WHITE
                    board[x][int(col/2)-1] = self._BLACK
                if x1 == (rw/2)+1:
                    board[x][int(col/2)] = self._BLACK
                    board[x][int(col/2)-1] = self._WHITE
        if start_color == 'W':
            for x in range(len(board)):
                x1 = x + 1
                if x1 == rw/2:
                    board[x][int(col/2)] = self._BLACK
                    board[x][int(col/2)-1] = self._WHITE
                if x1 == (rw/2)+1:
                    board[x][int(col/2)] = self._WHITE
                    board[x][int(col/2)-1] = self._BLACK                   
        self._board = board
        self.num_of_color()
      
        
    def _opposite_turn (self) -> str:
        if self._turn == 'B':
            return 'W'
        else:
            return 'B'

        
    ### CHECK PIECES ###

    def space_exists (self, row: int, column: int) -> bool:
        '''Checks if the coordinates exist on the board'''
        return -1 < row < len(self._board) and -1 < column < len(self._board[0])
        
        
    def space_is_empty (self, row: int, column: int) -> bool:
        '''True if that space is open, false if move DNE or piece already exists'''
        return self._board[row][column] == 0


    def BLACK_or_WHITE (self) -> int:
        if self._turn == 'B':
            return self._BLACK
        else:
            return self._WHITE
        
    def _opposite_color(self, x: int) -> int:
        if x == self._BLACK:
            return self._WHITE
        else:
            return self._BLACK

            
    ########### VALID MOVES (DIRECTION) ##########

    def check_down (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row+1, column) == False:
            return pieces_to_flip
        if self._board[row+1][column] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                row += 1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row+1][column] == current_color:
            return pieces_to_flip
        else:
            return pieces_to_flip

    def check_up (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)
        
        if self.space_exists(row-1, column) == False:
            return pieces_to_flip                              
        if self._board[row-1][column] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                row -= 1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row-1][column] == current_color:
            return pieces_to_flip
        
        else:
            return pieces_to_flip        
                

    def check_left (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row, column-1) == False:
            return pieces_to_flip                              
        if self._board[row][column-1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column -= 1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row-1][column] == current_color:
            return pieces_to_flip
        
        else:
            return pieces_to_flip        
        
    def check_right (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row, column+1) == False:
            return pieces_to_flip
        if self._board[row][column+1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column += 1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row][column+1] == current_color:
            return pieces_to_flip
        
        else:
            return pieces_to_flip 
                            
    def check_left_up (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row-1, column-1) == False:
            return pieces_to_flip                             
        if self._board[row-1][column-1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column -= 1
                row -=1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row-1][column-1] == current_color:
            return pieces_to_flip
        else:
            return pieces_to_flip         
                            
    def check_left_down (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row+1, column-1) == False:
            return pieces_to_flip                              
        if self._board[row+1][column-1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column -= 1
                row +=1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row+1][column-1] == current_color:
            return pieces_to_flip
        else:
            return pieces_to_flip 
                            
    def check_right_up (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row-1, column+1) == False:
            return pieces_to_flip                              
        if self._board[row-1][column+1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column += 1
                row -=1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row-1][column+1] == current_color:
            return pieces_to_flip
        else:
            return pieces_to_flip 
                                
    def check_right_down (self, row: int, column: int) -> list:
        pieces_to_flip = []
        potential_flippers = []
        current_color = self.BLACK_or_WHITE()
        opposite_color = self._opposite_color(current_color)

        if self.space_exists(row+1, column+1) == False:
            return pieces_to_flip                              
        if self._board[row+1][column+1] == opposite_color and self.space_is_empty(row, column):
            for each in range(len(self._board)):
                column += 1
                row +=1
                try:
                    if self._board[row][column] == opposite_color:
                        potential_flippers.append([row, column])
                    if self._board[row][column] == current_color:
                        return potential_flippers
                except:
                    return pieces_to_flip
        if self._board[row+1][column+1] == current_color:
            return pieces_to_flip
        
        else:
            return pieces_to_flip

                                               

    ########## FLIP PIECES & MAKE MOVE ##########

    def get_pieces_to_flip (self, row: int, column: int) -> ['coordinates']:
        '''Gathers all the pieces that flip into a list'''
        all_pieces = []
        
        all_pieces.extend(self.check_up(row, column))
        all_pieces.extend(self.check_down(row, column))
        all_pieces.extend(self.check_left(row, column))
        all_pieces.extend(self.check_right(row, column))
        all_pieces.extend(self.check_right_down(row, column))
        all_pieces.extend(self.check_right_up(row, column))
        all_pieces.extend(self.check_left_up(row, column))
        all_pieces.extend(self.check_left_down(row, column))

        return all_pieces       


    def flip_pieces (self, possible_flip: ['coordinates']):
        for coordinate in possible_flip:
            if len(coordinate) > 0:
                row = coordinate[0]
                column = coordinate[1]

                self._board[row][column] = self.BLACK_or_WHITE()


    def make_move(self, row:int, column: int):
        '''Makes move and returns INVALID if move DNE; returns VALID if move is possible'''
        move = [row, column]
        if move not in self.all_possible_moves():
            return('INVALID')
        if len(self.all_possible_moves()) == 0:
            return('WINNER: {}'.format(self.determine_winner()))

        else:
            self.flip_pieces(self.get_pieces_to_flip(row, column))
            self._board[row][column] = self.BLACK_or_WHITE()
            self._turn = self._opposite_turn()
            self.num_of_color()
#            self.print_board()
        
            if self.board_is_full() == True:
                return('WINNER: {}'.format(self.determine_winner()))
            else:
                pass
                
            
            
    ########## DETERMINING WINNER ##########

    def board_is_full(self) -> bool:
        '''Returns TRUE if there are no more moves on the board & the board is full'''
        answer = True
        for x in self._board:
            if 0 in x:
                answer = False
        return answer

    def determine_winner (self) -> 'winning color':
        winner = None
        black = self._black
        white = self._white
        b = 'B'
        w = 'W'
        tie = 'NONE'
        if self._gamestyle == '>': #player with most wins
            if black > white:
                return b
            elif white > black:
                return w
            elif black == white:
                return tie
        if self._gamestyle == '<':
            if black < white:
                return b
            elif white < black:
                return w
            elif black == white:
                return tie

    def all_possible_moves (self):
        down = len(self._board)
        across = len(self._board[0])
        indexes = []
        able_moves = []
        for x in range(down):
            for y in range(across):
                indexes.append([x, y])
                
        for coord in indexes:
            p = []
            q = self.get_pieces_to_flip(coord[0], coord[1])
            if len(q) > 0:
                p.append(q)
            if len(p) > 0:
                able_moves.append(coord)
        return able_moves
            
        
        

    ########## FUNCTIONS FOR BOARD ##########
            
    def num_of_color (self):
        totalblack = 0
        totalwhite = 0
        for x in self._board:
            for y in x:
                if y == 1:
                    totalblack +=1
                if y == 2:
                    totalwhite += 1
                    
        self._black = totalblack
        self._white = totalwhite
        
        
        
    def print_board(self):
        print('B: {}  W: {}'.format(self._black, self._white))
        for row in range(len(self._board)):
            b_string = ''
            for column in range(len(self._board[row])):
                if self._board[row][column] == self._NONE:
                    b_string += '.'
                elif self._board[row][column] == self._BLACK:
                    b_string += 'B'
                else:
                    b_string += 'W'
                b_string += ' '
            
            print(b_string)
        print('Turn: ' + self._turn)

    def get_black(self):
        return self._black

    def get_white(self):
        return self._white

    def get_board(self):
        return self._board



def create_board (row: int, column: int):
    '''Creates a visual grid'''
    game_board = []
    for i in range(row):
        game_board.append([])
        for x in range(column):
            game_board[-1].append(0)

    return game_board 
