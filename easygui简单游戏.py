import easygui as g
import sys

while 1:
        g.msgbox('Hello, world!')
        
        title = 'The most easy game in the world.'
        msg = 'What do you want now?'
        choices = ['Food', 'sleeping', 'Doing sport']

        choice = g.choicebox(msg, title,    choices)
        g.msgbox('Your choice is :'+ str(choice), 'result')

        msg = 'Do you want to restart the game?'
        title = 'Please make the choice.'
        if g.ccbox(msg, title):
                pass
        else:
                sys.exit(0)
        
        
        
	
	
	
	
	
	

