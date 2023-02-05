from check import move_rules
print
#chess board self explanotory piece is also explanatory newer x is the new value of the chess piece moved so is newer y
# x1 y1 are the old x and y positions white king x and white king y are the current position of the king  same with black 
# king x and back king y ok
# 
def check_logic(chess_board,piece,newer_x,newer_y,x1,y1,piece_color,white_king_x,white_king_y,black_king_x,black_king_y):
    ans=1
    rows=0
    chess_board[newer_y][newer_x]=piece_color+"_"+piece
    chess_board[y1][x1]=""
    if piece=="king" and piece_color=="white":
        for row in chess_board:
            
            cols=0
            for col in row:
                if col!="":
                    if col[0]=="b":
                        
                        if move_rules(chess_board,col.replace("black_",""),newer_x,newer_y,cols,rows,"black"):
                            ans=0
                cols+=1
            rows+=1
    elif piece=="king" and piece_color=="black":
        for row in chess_board:
            
            cols=0
            for col in row:
                if col!="":
                    if col[0]=="w":
                        
                        if move_rules(chess_board,col.replace("white_",""),newer_x,newer_y,cols,rows,"white"):
                            ans=0
                cols+=1
            rows+=1
    elif piece_color=="black" and piece!="king":
        rows=0
        for row in chess_board:
            cols=0
            for col in row:
                if col!="":
                    if col[0]=="w":
                        if move_rules(chess_board,col.replace("white_",""),black_king_x,black_king_y,cols,rows,"white"):
                            print(col.replace("white_",""),black_king_x,black_king_y,cols,rows)
                            ans=0
                cols+=1
            rows+=1
    elif piece_color=="white" and piece!="king":
        rows=0
        for row in chess_board:
            cols=0
            for col in row:
                if col!="":
                    if col[0]=="b":
                        if move_rules(chess_board,col.replace("black_",""),white_king_x,white_king_y,cols,rows,"black"):
                            ans=0
                cols+=1
            rows+=1
                        
                                         
    chess_board[y1][x1]=piece_color+"_"+piece
    chess_board[newer_y][newer_x]=""
    print(ans)
    if ans==1:
        return True          