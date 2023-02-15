import random as r
import os 

#Welcome and asking players for the number of players in start of game
print("      Welcome User! ")
numofplayers= int(input("Enter the number of players: "))

while (5 < numofplayers or numofplayers < 2):
      
     
      print("Number of players must be in between 2 and 5  ")
      numofplayers= int(input("Enter the number of players again: "))


#initializing variables 
checkers = ["X", "O", "R", "I", "S"]

#Initializing the board
NUM_ROWS = 11
NUM_COLS= 11
board=[]


#choosing a random player from 1 to number of players #switching turns 
def choose_player_turns():
    global checkers 
    return r.randint(0,numofplayers-1)


#creating the board
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
         row_list.append(' ')
    board.append(row_list)


# printing the board
def _board_():     
    #for i in range(0,NUM_ROWS ):
    for i in range(65, 65 + NUM_ROWS):
     print('   ',chr(i),' ',end='    ')
    # print(' ')
 
    print('\n')


    for i in range(0,NUM_ROWS ):
     print(i,end=' ')
     # print(i,end='\n')  
     for j in range(0,NUM_ROWS ):
    
      
       print('|__',board[i][j],' __|',end=' ') 
       
       
     print("\n") 
    #print(i)     
    
    
    
#assigning value 

def assigning_val_placing(player,a,b):
    sign=checkers[player-1]
    board[a][b]=sign
   



def _win_():


 def horizontal_win():
    

    hor_check=1
    for i in range(0,NUM_ROWS ):
     ch=board[i][0]
     for j in range(1,NUM_COLS ):
       
         if(board[i][j]==ch and ch!=' '):
          ch=board[i][j]
          hor_check=hor_check+1
    
         
     if(hor_check==NUM_COLS):      
         return True
         winner=ch  
      
     x=1
     hor_check=x
        

   
            
 #checking for a vertical win
 def vertical_win():
    
    ver_check=1
    for i in range(0,NUM_COLS ):
     ch=board[0][i]
     for j in range(1,NUM_ROWS):      
         if(board[j][i]==ch and ch!=' '):
          ch=board[j][i]
          word=ch
          ver_check=ver_check+1
    
     if(ver_check==NUM_ROWS):
         winner=ch  
         return True
     x=1
     ver_check=x  

    

 #checking for a diagnol win
 def first_diagnol_win():
    
    dia1_check=1
    for i in range(0,NUM_COLS ):
     ch=board[i][i]
     if(board[i][i]==ch and ch!=' '):
          ch=board[i][i]
          dia1_check=dia1_check+1
    
     if(dia1_check==NUM_ROWS+1):
          winner=ch  
          
          return True
   

 #checking for a left diagnol win
 def left_diagnol_win():
    
    dia2_check=1
    ch=board[0][NUM_COLS-1]
 
    for i in range(1,NUM_COLS ):
 
     if(board[i][NUM_COLS-i-1]==ch and ch!=' '):
          ch=board[i][NUM_COLS-i-1]
          dia2_check=dia2_check+1
    
     if(dia2_check==NUM_ROWS):
          winner=ch  
          
          return True
     
     
     
     
   
          
          

 left_diagnol_true= left_diagnol_win()
 right_diagnol_true=first_diagnol_win()
 verical_wining=vertical_win()
 horizantal_winning=horizontal_win()

 if(left_diagnol_win==True or right_diagnol_true==True or verical_wining==True or horizantal_winning==True ):
     
     return True

 else:
        return False
     
  
   


        
#return true if places not fied and fasle if place already filled
def validity_check(x,y):
#check for validity(invalid characters, out of board...)
 if(board[x-1][y-1]!=' '):
    print("place already filled")
    return False
 else:
    return True   




def choose_player_turns():
    global checkers 
    return r.randint(0,numofplayers-1)


#main

_board_()
c=True
a=choose_player_turns() +1
while(c):
  player_start = a
  if (a==numofplayers):
     a=1
  else:
    a=a+1


  print("Turn Of Player ")
  print(player_start)
 #ask player where to enter the sign
  total_moves=0
  chc=True
  #checking if player enter out of bound cordinates 
  while(chc):
    xy_cordi=input("Enter x and y corrdinates  ")
    xy      =list(xy_cordi)
    length_of_list=len(xy)
    if(length_of_list<=2):
     x_cordi_chr =xy[1]
     y_cordi_chr =xy[0] 
     leng=len(xy)
     x_cordi=int(ord(x_cordi_chr)-48)
     x_cordi=int(x_cordi+1)
     y_cordi=int(ord(y_cordi_chr)-64)
     #print(x_cordi,y_cordi)
 
   
     if(x_cordi<=NUM_COLS and y_cordi<=NUM_ROWS):
         chc=False
     elif(x_cordi>NUM_COLS and y_cordi<=NUM_ROWS):
         print("Not in range of numbers \n")
         #alphabets is out of range from board
     elif(y_cordi>NUM_ROWS and x_cordi<=NUM_COLS ):
       print("Alphabets is out of range from board")
     
     elif(x_cordi>NUM_COLS and y_cordi>NUM_ROWS):
       print("not xandycordinate")

    elif(length_of_list>2):
        y_cordi_chr =xy[0] 
        x_cordi_chr_1 =xy[1]
        x_cordi_chr_2 =xy[2]

        x_cordi_1=int(ord(x_cordi_chr_1)-48)
        x_cordi_1=int(x_cordi_1)
        
        x_cordi_2=int(ord(x_cordi_chr_2)-48)
        x_cordi_2=int(x_cordi_2+1)
        x_cordi=(x_cordi_1*10)+x_cordi_2

        y_cordi=int(ord(y_cordi_chr)-64)
        if(x_cordi>=NUM_ROWS+1 and y_cordi<NUM_COLS) :
            print("number out of range")
        elif(x_cordi>=NUM_ROWS+1 and y_cordi>=NUM_COLS):
            print("inappropriate input")

        else:
            chc=False





        
 #checking if sapce is already filled 
  ok=validity_check(x_cordi,y_cordi)
 
  while(ok==False):
    x_cordi= chr(input("Enter x cordinate again : "))
    y_cordi= chr(input("Enter y cordinate2 again: "))
    ok=validity_check(x_cordi,y_cordi)


  assigning_val_placing(player_start,x_cordi-1,y_cordi-1)
  total_moves+=1
  

  _board_()

  go=_win_()
  if(go==True):
   c=False
   print("winning player is ")
   print(player_start)
  elif(total_moves==NUM_ROWS*NUM_COLS and go==False):
   print("wohoo match is drawn")