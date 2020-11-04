import ST_classes
import random


#placement have to be set, to update player.board dict   FOR NOW NOT ACTIVE (object  put into player.board by list, no function etc)
#

#for now it is doubled HERE and in GUI

c1=ST_classes.creature("top")
c2=ST_classes.creature("center")
c3=ST_classes.creature("down")
c4=ST_classes.creature("top")
c5=ST_classes.creature("center")
c6=ST_classes.creature("down")

p1=ST_classes.player("Player1", 100)
p2=ST_classes.player("Player2", 100)
p1.show_board()


#replace with play/whatever the name   function

p1.board={"top":c1, "center":c2, "down":c3}
p2.board={"top":c4, "center":c5, "down":c6}




active_player = p1
inactive_player = p2


#some unittests XD

p1.race=p1.choose_race()
p2.race=p2.choose_race()
p1.pool_options(3)
p2.pool_options(2)
#p1.display_play()
#p2.display_play()



# main loop 
# WON'T BE USED as we do MVC, and it is a model part--> we need functions 
# which are used by controller
while True:
     p1.show_board()
     p2.show_board()
     active_player.display_play()
     active_player.play()
     for creature in active_player.board:
          if active_player.board[creature] == None: 
               continue
          else: 
               if active_player.board[creature].active == None:
                    print(f"{active_player.board[creature].name} inactive")
                    continue
               else: 
                    if inactive_player.board[creature] == None:
                         active_player.board[creature].attack(inactive_player)
                    else:
                         active_player.board[creature].attack(inactive_player.board[creature])
                
          if  active_player.board[creature] != None and active_player.board[creature].hp <1: 
               active_player.board[creature] = None             #KILLED OBJECTS still exist, but are out of the board
        
          if inactive_player.board[creature] != None and inactive_player.board[creature].hp <1: 
               inactive_player.board[creature] = None
     active_player.activate_all()
     active_player,inactive_player  = inactive_player, active_player
     #break# temporary



#some unittests XD
#c1.attack(c2)
print(c2.hp)
print(c4.hp)
print(p1.hp)
print(p2.hp)
print("\n")
for i,j in inactive_player.board.items():
    print(j)
print("\n")  
for i,j in active_player.board.items():
        print(j)
print("\n")  
p1.race=p1.choose_race()
p2.race=p2.choose_race()
p1.pool_options(4)
p2.pool_options(2)
p1.display_play()
p2.display_play()
p1.play()
