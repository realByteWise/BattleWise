#BattleWise v3.1 BIMBIMBAMBAM

from resources import *
import random,time

scroll("""Before starting, set IO font to Consolas and font size to '11'
Ready?""")
print()
ready=input("").lower()
if "n" in ready:
    print("Too bad.")
clear(24,1.5)
print("For peak gaming experience, please maximize Shell.")
clear(24,5)
print("""
                                     @@@@
                                    @@@@@@                                           
                  @@@@@   @@    @@  @@@@@@  @@@@@@@@   @@@@@@
                  @@  @@   @@  @@   @@@@@@     @@      @@
                  @@@@@     @@@@    @@@@@@     @@      @@@@@               
                  @@  @@     @@     @@@@@@     @@      @@               
                  @@@@@      @@     @@@@@@     @@      @@@@@@              
                                    @@@@@@                                 
                                    @@@@@@                                
                                    @@@@@@@@@@@@@@@@@@@@@@@@              
                                     @@@@@@@@@@@@@@@@@@@@@@@@              
                                      @@@@@@@@@@@@@@@@@@@@@@               
                                                                           
              @@@@@@@@@@@@@@@@@@@@@@@                                      
             @@@@@@@@@@@@@@@@@@@@@@@@@                                     
              @@@@@@@@@@@@@@@@@@@@@@@@@                                    
                                 @@@@@@                                    
                                 @@@@@@                            
             @@         @@  @@   @@@@@@    @@@@@   @@@@@@                   
             @@@   @   @@@  @@   @@@@@@   @@       @@                 
              @@@ @@@ @@@   @@   @@@@@@    @@@@    @@@@@@
               @@@@@@@@@    @@   @@@@@@       @@   @@
                @@@ @@@     @@   @@@@@@   @@@@@    @@@@@@                    
                                 @@@@@@                                    
                                  @@@@""")
clear(25,3)
scroll("In collaboration with Johan, Gleon and Nithin presents....")
clear(25,3)
print("""                          
  @@@@@@@     @@    @@@@@@@@ @@@@@@@ @@@     @@@@@@        
  @@@  @@@   @@@@      @@@     @@@   @@@     @@@         
  @@@@@@@@   @@@@@     @@@     @@@   @@@     @@@@@@        
  @@@@@@@@  @@@ @@@    @@@     @@@   @@@     @@@@@@           
  @@@  @@@@ @@@@@@@@   @@@     @@@   @@@@@@@ @@@       
  @@@@@@@@ @@@@  @@@@  @@@     @@@   @@@@@@@ @@@@@@
                                                                      +++
  ++++++++++++:--=+==========++++=+++++++++++++++++####    --       +++++##
  +++++++++++++++++++++++++++++++++++++++++++++++++####    ---     +++++++##
  +++++++++++++++++++++++++++++++++++++++++++++++++####      - --- ++++++###
  ++++++++++++++++++++++++++++++++++++++++++++++########   ----     ++++###
  ++++++++++++++++++++++++++++++++++++##################              ###                     
  ++++++++++++++++++++++++++++############                                           
  +++++++++++++++++++++++++++###                                @@@@    @@@@@@@     
  +++++++++++++=   ++=  =+++++###                 @@@@ @@@@   @@@@@@@@  @@@@@@@@     
  +++++++++=  =++= ++= +++  =++### @@@@     @@    @@@  @@@@  @@@@       @@@@         
  ++++++++=     +++@@@++     =+###  @@@@   @@@@  @@@@  @@@@  @@@@@      @@@@@@@@     
  ++++++++++++++++@@@@@+++++++++###  @@@  @@@@@@ @@@    @@@   @@@@@@@@   @@@@@@@@     
  +++=++++======++@@@@@======+++###   @@@@@@@@@@@@@@    @@@@    @@@@@@@  @@@@       
  ######++=    =+++@@@++=    =+###     @@@@@@@@@@@@     @@@@       @@@@   @@@@@@@@    
  ##  ###++= =+++  ++= =++= =++###     @@@@@@@@@@@@      @@@@  @@@@@@@@@  @@@@@@@@@   
       ###++++=    ++=   =++++###       @@@@  @@@@       @@@@   @@@@@@        
        ####++=    ++=  =+++####         @@    @@                                    
          ####++++++++++++####                                                       
            ######++++######                                                         
                ########""")
time.sleep(3)
scroll("""Do you dare to play?
 1. Yes
 2. No""")
print()
if int(input(""))==1:
    clear(25)
    scroll("""Choose your difficulty level (with caution):
 1. Easy    < Rajat :/ >
 2. Medium  < GENGHIS KHAN >
 3. Hard    < NAPOLEON BONAPARTE >
            ^^^^^^^^^^^^^^^^^^^^ WARNING!""")
    print()
    diff=int(input(""))
    if diff==1:
        import easy
        easy.game() #all dialogues are in the module
    elif diff==2:
        #same with this, just medium.game()
        #also im lazy to fix the rest ill do it later :P
        clear()
        print("""Looks like you like yourself a bit of a challenge eh?!..... i hope your ready
                                                             for whats coming""")
        time.sleep(1)
        clear()
        print("""Your face to face with genghis khans battle horde which has conqured the surplus
                                                 of nations this battle wont be an easy one""")
        time.sleep(1)
        clear()
        print("""The FIGHT HAS BEGUN Place your battle ships in strategic positions and Fight for glory
                                                                    or perish.......""")
        time.sleep(4)
        clear()
        import medium
        medium.game()
    elif diff==3:
        #here also; hard.game()
        clear()
        print("""Oh you think your ready to go against the GREAT EMPEROR NAPOLEON?
                                                            This battle shall be comical""")
        time.sleep(1)
        clear()
    
        print("""           %%%%%%###%%%%%%%%%%             
         %%%#####%%%#####%%%%%%%%%%%%        
      %%#######################%%%%%%%%      
    %%##%###################**###%%%%%%%%    
   %%#%####################**==+##%%%%%%%%   
  %%#%#######################**###%%%%%%%%%  
 %%#############################%%%%%%%%%%%% 
 %#############################%%%%%%%%%%%%% 
 %#%#########################%%%%%%%%%%%%%%%%
%%%%#######################%%%%%%%%%%%%%%%%%%
%%%%%%%%%################%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%******+#%%%%%%%*+++++++#%%%%      
     %**%%*+*+#%**++*#%+***+*##++++#%++*%    
    %++*#%+++++=+**+*===++**++++++=#%*+=*    
    %++**%+=++++++++*===++=++++++==*#+++#    				"You think you can defeat me?? Mortal
    %#+++*========+*++++++*+=======+*++*%    
      ##**=======++++++++*+++======+##%      
      %###======+====+**+====+=====+%%       
     %####*=======**********======+###%      
    %########*======++++++=====+#%#####%     
   %%#######%%#++==+**+*++==***#%%######%    
   %#####*#***###+=====+++*+###***######%%   
   %#############+=======+*+*###########%%   
   %%############+======++*+*###########%%   
    %%########+*#*===++*+*++##**########%    
       %%%%%##%%%%%%**#%%##%%%%%#%%%%%%%   """)
        time.sleep(1)
        clear()
        
        print("""You find yourself on the battle field of the french revolution the great napolean
                                    has sent his fleet to destroy you place your warships
                                              and defend your nation   """)
        time.sleep(4)
        clear()
        import hard
        hard.game()
    else:
        scroll("That's not... a choice? Okay... thanks for playing!")

else:
    clear(25)
    scroll("B r u h . ",0.1)
    scroll("Coward ahh move but alright!")
