from termcolor import colored, cprint
import colorama
colorama.init()
HeroWin = 0
LopoWin = 0
TemaWin = 0
KeevaWin = 0
FinalHeroWin = 0
FinalDragWin = 40
cprint('Hello!', 'blue')

whatstory = input("Which adventure would you like to go on today a for the main quest, b for a more difficult side quest one? ")
if whatstory == "a":
  print("You have chosen the the main quest, regardless of your choice")
  print('on this quest you will make many decisions that will impact whether')
  print('you succed or not. Choose carfuly and good luck.')
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
      FinalHeroWin += 40
      cprint('you chose option a <We have no need>', 'cyan')
      cprint('Beowa: Are you sure, protection is very important in these times', 'blue')
      speakchoice1a = input('how do you respond a.Yes b. Pretty sure c.actually, maybe not')
      if speakchoice1a == 'a':
          FinalHeroWin += 90
      elif speakchoice1a == 'b':
          FinalHeroWin += 30
      elif speakchoice1a == 'c':
          FinalHeroWin += 40
    elif speakchoice1 == 'b':
      FinalHeroWin += 40 
      cprint('you chose option b <We just need a few troops>', 'cyan')
      cprint('Beowa: Are you sure, this might be an all or nothing decison', 'blue')
      speakchoice1b = input('how do you respond a.Yes b. Pretty sure c.actually, maybe not')
      if speakchoice1b == 'a':
          FinalHeroWin += 80
      elif speakchoice1b == 'b':
          FinalHeroWin += 10
      elif speakchoice1b == 'c':
          FinalHeroWin += 200
    elif speakchoice1 == 'c':
      FinalHeroWin +=  20
      cprint('you chose option c <We need as many troops as possible>', 'cyan')
      cprint('Beowa: Are you sure, We are much more powerful than they are, this could be a waste of important resources', 'blue')
      speakchoice1c = input('how do you respond a.Yes b. Pretty sure c.actually, maybe not')
      if speakchoice1c == 'a':
          FinalHeroWin += 150
      elif speakchoice1c == 'b':
          FinalHeroWin += 82
      elif speakchoice1c == 'c':
          FinalHeroWin += 24      
    cprint('Beowa: Very well then. Oh, that reminds me, You must choose your generals.', 'blue')
    cprint('Your generals may be the most important part of your quest', 'yellow')
    cprint('Have faith in your generals and they will have faith in you', 'yellow')
    cprint('Make sure you work with your generals and have faith in them to succeed.', 'yellow')
    continue2Lopo = input("press the a key to meet your first general" )
    if continue2Lopo == "a": 
      cprint('Lopo: Hello I am Lopo, I am a sword fighter, I trained under the legendary Wiglaf', 'blue') 
      cprint('My master and I were responsible for saving the geats from Anihilation', 'blue' )
      continue2Tema = input("press the a key to meet the next general member")
      if continue2Tema == "a": 
        cprint('Tema: Hello I am Tema, I am an archer/mage', 'blue')
        cprint('I used the knowlege a gained from studying under lengendary Magicians to develop my technique.', 'blue')
        cprint('I use my magic to shoot my arrows at light speed with deathly accuracy.', 'blue')
        continue2Keeva = input("press the a key to meet your third general" )
        if continue2Keeva == "a": 
          cprint('Keeva: Hello: I am Keeva, for 15 years I Lead my armies', 'blue') 
          cprint('through the frigid winters of Aelthgar, expanding our nations power and influence', 'blue')
          cprint('I have faith that your will be the leader we need to keep our nation safe', 'blue')
          continue2ultweapon = input("press the a key to continue")
          if continue2ultweapon == "a":
           cprint('Tema: We should not under estimate the power of the Unfearths.', 'blue')
           cprint('Lopo: and why is that? time after time we have put them in their place', 'blue')
           cprint('Tema: while that may be true, one of our spies recently discovered plans', 'blue')
           cprint('discussing some kind of ultimate weapon to destroy us', 'blue')
           cprint('Tema: are either of your familiar with the Myth of Varselgorva?', 'green')
           Vquestion = input('a. Of course b. Of what')
           if Vquestion == 'a':
            cprint('Tema: Good, then you know why this is such a great threat', 'blue')
           if Vquestion == 'b':
            cprint('Tema: Ok, Ill let Keeva explain', 'blue')
            cprint('Keeva: Long ago, an evil alchemist Ostanes created a horrific creature', 'blue')
            cprint('So horrific that reciting its name in its original language would', 'blue')
            cprint('kill any one who had the misfortune of hearing it', 'blue' )
            cprint('Lopo: Tema and I, with the assistance of a mythical Theiko known as Hertha', 'blue')
            cprint('Disposed of him many years ago', 'blue')
            cprint('Tema: But know he may have been back being used as a slave for the Unferths', 'blue')
            Continue0 = input('press a to continue')
            if Continue0 == 'a':
             cprint('All Generals: And that is why we need to unite our people to save the shieldings from doom!')
          cprint('Narrator: And so you and the Generals join forces to defeat the Unferthean menace', 'green')
          cprint('To Be Continued')
          print('Final score =') 
          print(FinalHeroWin)



elif whatstory == "b":
  print("You have chosen the more difficult side quest")
  print("Welcome to Allborg, on this quest you will make many decisions that will impact whether you succed or not. Choose carfuly and good luck ")
  continue1 = input("press the a key to continue")
  if continue1 == "a":
    print('Your quest starts in a hall of gods')