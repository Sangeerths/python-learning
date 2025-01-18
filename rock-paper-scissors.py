
import random , sys

print("ROCK , PAPER , SCISSOR ")
win=0
loss=0
ties=0
while(True):
    print("%s wins , %s ties %s loss ",(win,ties,loss))
    print("Enter your move: (r)ock , (p)aper, (s)cissors and (q)uit")  # enter the player move
    playermove=(input())
  # player move from the user input
    if(playermove=='q'):   
        sys.exit(0)
    if(playermove=='r'):
        print("ROCK versus ....")
    if(playermove=='p'):
        print("PAPER versus ...")
    if(playermove=='s'):
        print("SCISSORS versus ...")
        # sytem moves which is acqiured using random number
    random_num=random.randint(1,3)
    if(random_num== 1):
        computermove='r'
    if(random_num== 2):
        computermove='p'
    if(random_num==3):
        computermove='s'
       #comparing the moves 
    if(playermove==computermove):
        print("It is a tie..")
        ties=ties+1
    if(playermove=='r' and computermove=='p'):
        print("You lose")
        loss=loss+1
    if(playermove=='p' and computermove=='s'):
        print("You lose ..")
        loss=loss+1
    if(playermove=='s' and computermove=='r'):
        print("You lose. ")
        loss=loss+1
    if(playermove=='p' and computermove=='r'):
        print("you win ..")
        win=win+1
    if(playermove=='s' and computermove=='p'):
        print("You win ")
        win=win+1
    if(playermove=='r' and computermove=='s'):
        print("You win. ")
        win=win+1
        
        
        
        
        
        
