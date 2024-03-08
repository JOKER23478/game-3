#Name:Youssef Abd Al Razzak Adel Abd Al Razzak            #Game Description: You start with a number and the two players subtract this number with a perfect square root number like (1,4,9,16...) and the player who reaches the number zero first is the winner 
#ID:20231212
print("subtract a square\n It is a game which the players put a number and begin to subtract the number with a perfect square root number \n the player who reach number 0 first is the winner ")
while True:
   try:  
      Num_coins=int(input("enter a number from(10-1000):\n "))
      if 10<=Num_coins<=1000:
       break
   except ValueError:
      print("Error!invalid input")

        

 


import math    #to use the square root from the library
def update_state (coins_taken):
    global Num_coins
    Num_coins -= coins_taken     #to subtract the number of coins that the player entered from the number of coins that was already been entered before 



#Knowing the winner when the player reaches zero 
def is_winner():
    global Num_coins
    if Num_coins<=0:
      return True
    


    
   


#Making the rules of the game  
 
     #Making the rules for player 1 
while True :
    while True :  
        try :
            subtracted_coins1=int(input("player 1 enter a perfect square root number:\n "))
            while subtracted_coins1<=0 or subtracted_coins1>Num_coins  or subtracted_coins1 % math.sqrt(subtracted_coins1)!=0:
               subtracted_coins1=int(input("invalid number,Enter a number has a square root:\n "))
            break
        except ValueError :
           print("Error!unvalid number")
    
    update_state(subtracted_coins1)
      #to get the right input
    
    if is_winner():
        print("Player 1 is the winner \n Game has ended")
        break
    else:
        print("reminder number of coins: ",Num_coins)
        



        
        #Making the rules for player 2 
        while True:
           try :
               subtracted_coins2=int(input("player 2 enter a number has square root:\n ")) 
               while subtracted_coins2<=0 or subtracted_coins2>Num_coins  or subtracted_coins2 % math.sqrt(subtracted_coins2)!=0:
                   subtracted_coins2=int(input("invalid number,Enter a number has a square root:\n ")) 
               break
           except ValueError : 
              print("Error!unvalid number")
        
        #to get the right input
        update_state(subtracted_coins2)
        if is_winner():
            print("Player 2 is the winner \n Game has ended")
            break
        else :
                 print("Reminder number of coins: ",Num_coins)
          
    