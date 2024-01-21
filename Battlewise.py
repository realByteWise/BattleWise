import random
import time
def clear2():
    for hu in range(24):
        print("")
def clear():
    time.sleep(1)
    for _ in range(40):
        print("")    
print("Please maximize shell window for best experience......")
time.sleep(5)
print("""                                
                                    @@@@@@                                 
                                    @@@@@@                                 
                                    @@@@@@                                 
                  @@@@@     @@@ @@@ @@@@@@ @@@@@@@     @@@@@@              
                  @@@@@      @@@@   @@@@@@    @@       @@@@@               
                  @@@@@@      @@    @@@@@@    @@       @@@@@               
                  @@@@@       @@    @@@@@@    @@       @@@@@@              
                                    @@@@@@                                 
                                    @@@@@@                                 
                                    @@@@@@@@@@@@@@@@@@@@@@@@@              
                                    @@@@@@@@@@@@@@@@@@@@@@@@@              
                                     @@@@@@@@@@@@@@@@@@@@@@@               
                                                                           
               @@@@@@@@@@@@@@@@@@@@@@                                      
             @@@@@@@@@@@@@@@@@@@@@@@@@                                     
              @@@@@@@@@@@@@@@@@@@@@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
               @@ @@@ @@     @@  @@@@@   @@@@@    @@@@@@                   
                @@@@@@@@     @@  @@@@@  @@@       @@@                
                @@@ @@@      @@  @@@@@  @@@@@@    @@@@@@                   
                 @@  @       @@  @@@@@   @@@@     @@@@@@                    
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@                                     
                                 @@@@@""")
time.sleep(1)
clear()
print("In collaboration with Johan Gleon And Nithin presents to you........")
clear2()
time.sleep(3)
clear()
print("""                          
  @@@@@@@     @@    @@@@@@@@ @@@@@@@ @@@     @@@@@@        
  @@@  @@@   @@@@      @@@     @@@   @@@     @@@         
  @@@@@@@@   @@@@@     @@@     @@@   @@@     @@@@@@        
  @@@@@@@@  @@@ @@@    @@@     @@@   @@@     @@@@@@           
  @@@  @@@@ @@@@@@@@   @@@     @@@   @@@@@@@ @@@       
  @@@@@@@@ @@@@  @@@@  @@@     @@@   @@@@@@@ @@@@@@
  
  ++++++++++++:--=+==========++++=+++++++++++++++++++++    --        ++++
  +++++++++++++++++++++++++++++++++++++++++++++++++++++    ---      ++++++
  +++++++++++++++++++++++++++++++++++++++++++++++++++++      - --- ++++++++  
  +++++++++++++++++++++++++++++++++++++++++++++++++++++=   ----     ++++++
  ++++++++++++++++++++++++++++++++++++++++++++++++++=+++             ++++
  +++++++++++++++++++++++++++++++++++++=     
  +++++++++++++++++++++=+++++++         
  +++++++++==++=  =+=   =+++++++=      
  +++++++++   +++==+= +++=  =++++       
  ++++++++=     =++++++=    +++++=                      
  ++++++++++++++++++++++++++++++++                         
  ++++++++      +++++++=     +++++                         
  ++==++++=    ++=+++=++=   =++++=                         
  ==  +++++  ++=  =+=  =++= +++++                          
       +++++++=   =+=    =++++++                           
        =+++++=   =+=  ==++++++                            
         =+++++++++++++++++++=                             
            =+++++++++++++=         """)
time.sleep(3)
clear()

if input("Do you dare to play? (Yes/no)").upper()=="YES":
    clear()
    print("Choose your difficulty level ( With Caution ):")
    print("1.Easy ")
    print("2.Medium < GENGHIS KHAN >")
    print("3.Hard  <NAPOLEAN BONEPART>")
    diff=input("").upper()
    if diff=="EASY":
        clear()
        print(""" You find yourself on the battle field the enemy has sent battle ships to take over the port
                     Place your battle ships wiseley and GET READY TO FIGHT""")
        time.sleep(4)
        clear()
        import easy
        easy.game()
    elif diff=="MEDIUM":
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
    elif diff=="HARD":
        clear()
        print("""Oh you think your ready to go against the GREAT EMPEROR NAPOLEON?
                                                            This battle shall be comical""")
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
        print("Invalid choice. Exiting...")

else:
    print("Aerhhdfgh you've escaped... for now")
