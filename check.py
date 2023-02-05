def move_rules(chess_board,piece,new_x,new_y,x,y,piece_color):
    print
    ans=0
    check=0
   
    if True:
        pass
        if piece=="pawn1":
            if piece_color=="white":   
                
                if (new_x==x and new_y==y-1) or (new_y==y-2 and new_x==x ):
                    
                    if chess_board[new_y][new_x]=="":
                        
                        ans=1
                        
                
                    
                    
                    
                
                elif (new_x==x+1 or new_x==x-1) and new_y==y-1:
                    
                    if chess_board[new_y][new_x]!="":
                        ans=1
            if piece_color=="black":
                if new_x==x and (new_y==y+1 or new_y==y+2):
                    if chess_board[new_y][new_x]=="":
                        ans=1
                elif (new_x==x+1 or new_x==x-1) and new_y==y+1:
                    if chess_board[new_y][new_x]!="":
                        ans=1
        
        
        elif piece=="pawn":
            if piece_color=="white":   
                
                if new_x==x and new_y==y-1:
                    
                    if chess_board[new_y][new_x]=="":
                        
                        ans=1
                        
                
                    
                    
                    
                
                elif (new_x==x+1 or new_x==x-1) and new_y==y-1:
                    
                    if chess_board[new_y][new_x]!="":
                        ans=1
            if piece_color=="black":
                if new_x==x and new_y==y+1:
                    if chess_board[new_y][new_x]=="":
                        ans=1
                elif (new_x==x+1 or new_x==x-1) and new_y==y+1:
                    if chess_board[new_y][new_x]!="":
                        ans=1
                
                       
                   
       
        
                
                
        elif piece=="knight":
                if (new_y==y+2 or new_y==y-2) and (new_x==x+1 or new_x==x-1):
                    return True
                elif (new_y==y+1 or new_y==y-1) and (new_x==x+2 or new_x==x-2):
                    return True
        elif piece=="rook":
            
            if (new_x != x and new_y == y) or (new_y != y and new_x == x):
                
                if new_x==x:
                    if new_y<y:
                        new_y,y=y,new_y
                  
                    for i in range(new_y-1,y,-1):
                        if chess_board[i][x]!="":
                            check=1
                    if check!=1:
                        ans=1
                else:
                    if new_x<x:
                        new_x,x=x,new_x
                    for i in range(new_x-1,x,-1):
                        if chess_board[y][i]!="":
                              check=1
                    if check!=1:
                        ans=1
        elif piece=="bishop":
            
            
            if abs(new_x-x)==abs(new_y-y):
               
                if (new_x>x and new_y>y) or (new_y<y and new_x<x):
                    
                    if new_y<y:
                        
                        new_y,y=y,new_y
                        new_x,x=x,new_x
                   
                    for i in range(y+1,new_y):
                        
                        x+=1
                        
                        if chess_board[i][x] !="":
                            check=1
                    
                    if check != 1:
                        ans=1
                elif(new_x>x and new_y<y) or (new_y>y and new_x<x):
                    
                    if new_x<x:
                        new_x,x=x,new_x
                        new_y,y=y,new_y
                    for i in range(new_x-1,x,-1):
                        new_y+=1
                        
                        if chess_board[new_y][i]!="":
                            check=1
                    if check!=1:
                        ans=1
        elif piece=="queen":
            
            if abs(new_x-x)==abs(new_y-y):
               
                if (new_x>x and new_y>y) or (new_y<y and new_x<x):
                    
                    if new_y<y:
                        
                        new_y,y=y,new_y
                        new_x,x=x,new_x
                   
                    for i in range(y+1,new_y):
                        
                        x+=1
                        
                        if chess_board[i][x] !="":
                            check=1
                    
                    if check != 1:
                        ans=1
                elif(new_x>x and new_y<y) or (new_y>y and new_x<x):
                    
                    if new_x<x:
                        new_x,x=x,new_x
                        new_y,y=y,new_y
                    for i in range(new_x-1,x,-1):
                        new_y+=1
                        
                        if chess_board[new_y][i]!="":
                            check=1
                    if check!=1:
                        ans=1
            elif (new_x != x and new_y == y) or (new_y != y and new_x == x):
            
                if new_x==x:
                    if new_y<y:
                        new_y,y=y,new_y
                  
                    for i in range(new_y-1,y,-1):
                        if chess_board[i][x]!="":
                            check=1
                    if check!=1:
                        ans=1
                else:
                    if new_x<x:
                        new_x,x=x,new_x
                    for i in range(new_x-1,x,-1):
                        if chess_board[y][i]!="":
                              check=1
                    if check!=1:
                        ans=1           
        elif piece=="king":
            if  abs(new_x-x)==1 and abs(new_y-y)==1:
                
                ans=1
            elif abs(new_x-x)==1 and new_y==y:
                ans=1
            elif abs(new_y-y)==1 and new_x==x:
                ans=1
    if ans==1:
        return True      