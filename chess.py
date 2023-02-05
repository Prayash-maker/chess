import pygame
from checklogic import check_logic
from check import move_rules
black_pawn=pygame.image.load("black_pawn.png")
black_rook=pygame.image.load("black_rook.png")
black_knight=pygame.image.load("black_knight.png")
black_bishop=pygame.image.load("black_bishop.png")
black_queen=pygame.image.load("black_queen.png")
black_king=pygame.image.load("black_king.png")

allow=False
white_king_x,white_king_y=4,7
black_king_x,black_king_y=4,0
white_pawn=pygame.image.load("white_pawn.png")
white_rook=pygame.image.load("white_rook.png")
white_knight=pygame.image.load("white_knight.png")
white_bishop=pygame.image.load("white_bishop.png")
white_queen=pygame.image.load("white_queen.png")
white_king =pygame.image.load("white_king.png")
turn=0
pygame.init()
chess_board=[["black_rook","black_knight","black_bishop","black_queen","black_king","black_bishop","black_knight","black_rook"],
            ["black_pawn1"]*8,
            [""]*8,
            [""]*8,
            [""]*8,
            [""]*8,
            ["white_pawn1"]*8,
            ["white_rook","white_knight","white_bishop","white_queen","white_king","white_bishop","white_knight","white_rook"]]



pygame.display.set_caption("chess")
black_square=(0,0,0)
light_square=(255,255,255)


screen = pygame.display.set_mode((800, 800))
for row in range(8):
    for col in range(8):
        if (row+col)%2==0:
            square_color=light_square
        else:
            square_color=black_square
        pygame.draw.rect(screen,square_color,(row*100,col*100,100,100))
        
for row in range(8):
    for col in range(8):
        if row==1:
            screen.blit(black_pawn,(col*100,100))
        if row==0:
            if col==0 or col==7:
                screen.blit(black_rook,(col*100,row*100))
            if col==1 or col==6:
                screen.blit(black_knight,(col*100,row*100))
            if col==2 or col==5:
                #bishop
               screen.blit(black_bishop,(col*100,row*100))
            if col==3:
                #queen
                screen.blit(black_queen,(col*100,row*100))
            if col==4:
                #king
                screen.blit(black_king,(col*100,row*100))
        if row==6:
            screen.blit(white_pawn,(col*100,row*100))
        if row==7:
                if col==0 or col==7:
                    screen.blit(white_rook,(col*100,row*100))
                if col==1 or col==6:
                    screen.blit(white_knight,(col*100,row*100))
                if col==2 or col==5:
               
                    screen.blit(white_bishop,(col*100,row*100))
                if col==3:
                
                    screen.blit(white_queen,(col*100,row*100))
                if col==4:
                    screen.blit(white_king,(col*100,row*100))

pygame.display.update()        

allow_movement=False
selected=False
rows=-1

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                new_x,new_y=event.pos
                if chess_board[int(new_y/100)][int(new_x/100)] != "" and selected==False:
                    selected=True
                    x,y=new_x,new_y
                elif selected==True:
                    
                    selected=False
                    if chess_board[int(new_y/100)][int(new_x/100)]=="":
                        chess_board[int(new_y/100)][int(new_x/100)]="empty"
                    if chess_board[int(new_y/100)][int(new_x/100)][0] != chess_board[int(y/100)][int(x/100)][0]:
                        if new_x != x and new_y !=y:
                            new_x_2d=int(x/100)
                            new_y_2d=int(y/100)
                           
                            if chess_board[new_y_2d][new_x_2d][0]=="b":
                                piece=chess_board[new_y_2d][new_x_2d].replace("black_","")
                                piece_color="black"
                            elif chess_board[new_y_2d][new_x_2d][0]=="w":
                                piece=chess_board[new_y_2d][new_x_2d].replace("white_","")
                                piece_color="white"
                            if chess_board[int(new_y/100)][int(new_x/100)]=="empty":
                                chess_board[int(new_y/100)][int(new_x/100)]=""
                                
                            if move_rules(chess_board,piece,int(new_x/100),int(new_y/100),new_x_2d,new_y_2d,piece_color):
                                
                                if piece_color=="white" and turn%2==0:
                                    allow=True
                                elif piece_color =="black" and turn%2==1:
                                    allow =True
                                
                                    
                                if piece=="king" and piece_color=="white":
                                        white_king_x,white_king_y=int(new_x/100),int(new_y/100)
                                elif piece=="king" and piece_color=="black":
                                        black_king_x,black_king_y=int(new_x/100),int(new_y/100)
                                
                                if check_logic(chess_board,piece,int(new_x/100),int(new_y/100),new_x_2d,new_y_2d,piece_color,white_king_x,white_king_y,black_king_x,black_king_y) and allow==True:
                                    
                                    chess_board[int(new_y/100)][int(new_x/100)]=chess_board[int(y/100)][int(x/100)]
                                    chess_board[int(y/100)][int(x/100)]=""
                                    turn+=1
                                    allow=False
                                    
                                    if piece=="pawn1":
                                       
                                        chess_board[int(new_y/100)][int(new_x/100)]=piece_color+"_"+"pawn"
                                    
                                    for row in chess_board:
                                        rows+=1
                                        cols=-1
                                        for col in row:
                                            cols+=1
                                            if col != "" and col !="empty":
                                                image=col+".png"
                                                pieces=pygame.image.load(image)
                                                screen.blit(pieces,(cols*100,rows*100))
                                            elif col=="" or col =="empty":
                                            
                                                if(rows+cols)%2==0:
                                                    square_color=light_square
                                                else:
                                                    square_color=black_square
                                                pygame.draw.rect(screen,square_color,(cols*100,rows*100,100,100))            
                      
                                rows=-1   
                        
           
    pygame.display.update()
pygame.quit()




       
                        
                        
                    
                    
                    
                    
                    
                     
                        
                        

