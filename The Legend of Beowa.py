
from  termcolor import colored, cprint
import colorama
colorama.init()
HeroWin = 0
LopoWin = 0
TemaWin = 0
FinalHeroWin = 0
FinalDragWin = 40
cprint('Hello!', 'blue')

whatstory = input("Which adventure would you like to go on today a for an easy one, b for a more difficult one? ")
if whatstory == "a":
  print("You have chosen the the easier quest, regardless of your choice, on this quest you will make many decisions that will impact whether you succed or not. Choose carfuly and good luck ")
  continue1 = input("press the a key to continue")
  if continue1 == "a":
    print('You begin in the Massive palace of Hereot discussing matters with the old Queen Beowa')
    print('You are the Queen first in command ')
    cprint('Beowa: We live in an age of peace, we have yet to have any sort of attack', 'blue')
    cprint('however this worrys me as rumors have come up saying that the Unfearthean army is planning an attack', 'blue')
    cprint("They are significantly weaker but I'm still fearfull of them", 'blue')
    cprint('Are my feelings warranted?', 'green')
    cprint("What do you say to Beowa [you want to be honest to her, but still keep please her]", 'yellow')
    cprint('a. We have no need b. We just need a few troops c. We need as many troops as possible', 'cyan')
    speakchoice1 = input('what do you choose') 
    if speakchoice1 == 'a':
      FinalHeroWin += 2
      cprint('you chose option a <We have no need>', 'cyan')
      cprint('Beowa: Are you sure, protection is very important in these times', 'blue')
      cprint('how do you respond a.Yes b. Pretty sure c.actually, maybe not', 'yellow')
    elif speakchoice1 == 'b':
      FinalHeroWin += 40 
      cprint('you chose option b <We just need a few troops>', 'cyan')
      cprint('Beowa: Are you sure, this might be an all or nothing decison', 'blue')
      cprint('how do you respond a.Yes b. Pretty sure c.actually, maybe not', 'yellow')
    elif speakchoice1 == 'c':
      FinalHeroWin +=  60
      cprint('you chose option c <We need as many troops as possible>', 'cyan')
      cprint('Beowa: Are you sure, We are much more powerfull than they are, this could be a waste of important resources', 'blue')
      cprint('how do you respond a.Yes b. Pretty sure c.actually, maybe not', 'yellow')
      


elif whatstory == "b":
  print("You have chosen the more challenging quest")
  print("Welcome to Allborg, on this quest you will make many decisions that will impact whether you succed or not. Choose carfuly and good luck ")
  continue1 = input("press the a key to continue")
  if continue1 == "a":
    print('Your quest starts in a hall of gods')