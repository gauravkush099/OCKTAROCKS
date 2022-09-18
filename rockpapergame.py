import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game start
1 Game start
2 No |exit
    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
           1 rock
           2 scissor
           3 paper
            
            '''))
            if userinput==1:
                uchoice='rock'
            elif userinput==2:
                uchoice='scissor'
            elif userinput==3:
                uchoice='paper'
            cchoice=random.choice(l)
            if  uchoice==cchoice:
                print('computer value',cchoice)
                print('uservalue',uchoice)
                print('Game Draw')
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=='rock'and cchoice=='scissor'
                  or uchoice=='paper'and cchoice=='rock'
                  or uchoice=='scissor'and cchoice=='paper'):
                print('computer value', cchoice)
                print('uservalue', uchoice)
                print('You win')
                ucount = ucount + 1
            else:
                print('computer value', cchoice)
                print('uservalue', uchoice)
                print('computer win')
                ccount = ccount + 1
        if    uc==ccount:
              print('Final game draw')
              print('user score',ucount)
              print('computer score',ccount)
        elif  uc>ccount:
              print('Finaly you win the Game')
              print('user score', ucount)
              print('computer score', ccount)
        else:
              print('Finaly computer win the game')
              print('user score', ucount)
              print('computer score', ccount)
    else:
        break