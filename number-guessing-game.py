#number guessing game 
import random
def game():
    
    logo='''
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
                                                                                    
'''  
    print(logo)
    inp=int(input("Welcome to the Number guessing game!\nChoose the level of Difficulty:\n1.Easy\n2.Medium\n3.Hard\n"))  
    def level(num):
        if(inp==1):
           return 10
        elif(inp==2):
           return 7
        elif(inp==3):
           return 5 
    lev=level(inp) 
    easy=10
    hard=5
    medium=7
    answer=random.randint(1,100) 
    num=0
    while(num!=answer ):
        num=int(input("Enter your guess:\n")) 
        lev-=1
        if(num==answer):
            print(f"Good job! Correct answer is {answer}")
        elif(num>answer):
            print(f"Too high\n{lev} chances left out of {level(inp)}")
        else:
            print(f"Too low\n{lev} chances left out of {level(inp)}")
        if(lev==0):
            break 
        
game()