import random as rn

class ttt:

    def __init__(self):
        # board
        self.board = [0 for _ in range(9)]
        # x is 0, y is 1
        self.player = 0
        # position 0-8
        self.valid_positions = list(range(9))
        self.winner = "tie"

    def __str__(self):
        b = ""
        for i in [self.board[0:3],self.board[3:6],self.board[6:]]:
                b += "{0:<3} {1:<3} {2:<3}\n".format(*i)
        return b

    def player_letter(self):
        return (self.player % 2 == 0)*'x' or (self.player % 2 != 0)*'y'  
    
    # y's strategy to pick corners, then middle, then sides
    # you will rewrite this to improve y's strategy
    # return a list [(pos,score),(pos,score),...]
    # where pos are the possible remaining positions to pick
    # and score is some non-negative value reflecting the goodness
    # of the position
    # you can use possibly the win method too
    def best_next_move(self):
        scored = []
        for p in self.valid_positions:
                if p in (0,2,6,8):
                    scored.append((p,2))
                elif p in (1,3,5,7):
                    scored.append((p,1))
                else:
                    scored.append((p,3))
        return scored
    
    def next_move(self,*moves):
        #if you send a list of moves [(pos,score),(pos,score),...]
        #then 'y' will choose the best
        if moves:
            moves = moves[0]
            moves.sort(key = lambda x:x[1],reverse = True)
            square = moves[0][0]
        else:
        #otherwise 'y' picks randomly
            square = rn.choice(self.valid_positions)
        self.board[square] = self.player_letter()
        # print(f"{self.player_letter()} plays {square}")
        self.valid_positions.remove(square)
        # print(f"board looks like: {self.valid_positions}")
            
    def play_game(self):
        while self.valid_positions:
            #uncomment to see best moves
            # print(f"{self.player_letter()} scored moves:")
            # print(f"{self.best_next_move()}")

            #use this to improve y's strategy
            #comment out no strategy
            if self.player_letter() == 'y':
                # print(f"next best move {self.best_next_move()}")
                self.next_move(self.best_next_move())
            else:
                self.next_move()
            
            #no strategy
            # self.next_move()
            
            if self.win():
                self.winner = self.player_letter()
                break
            self.player = 1 - self.player
        return self.winner

    def win(self):
        k = [self.player_letter() for _ in range(3)]
        r0 = self.board[0:3]
        r1 = self.board[3:6]
        r2 = self.board[6:]
        c0 = [self.board[0],self.board[3],self.board[6]]  
        c1 = [self.board[1],self.board[4],self.board[7]]
        c2 = [self.board[2],self.board[5],self.board[8]]
        d0 = [self.board[0],self.board[4],self.board[8]]
        d1 = [self.board[2],self.board[4],self.board[6]]
        return k in [r0,r1,r2,c0,c1,c2,d0,d1]

game = ttt()
# print(game.play_game())

outcome = {'x':0,'y':0,'tie':0}

for _ in range(100000):
    outcome[game.play_game()] += 1
    game = ttt()
print(outcome)