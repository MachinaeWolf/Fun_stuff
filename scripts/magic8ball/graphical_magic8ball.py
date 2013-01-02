# imports everything from the graphics.py library so you don't have to prefix every graphics command with graphics. like graphics.GraphWin for example 
# NOTE: Must have the graphics.py file in the same directory as graphical_magic8ball.py or the program Will NOT run properly.

from graphics import *
# imports only the random.choice command so you can just use the command choice
from random import choice
# imports only the time.sleep commmand so you can just use the command sleep
from time import sleep


#magic8ball with a gui
def run(windowScreen, circle):
	# list of answers the 8ball gives you
	eightBall_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely!", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook is good.", "Yes!", "All signs point to yes.", "Reply hazy, try again.", "Ask again later.", "I can't tell you now.", "Can't predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook is not so good.", "Very doubtful."]
	# randomly picks text from the list
	eightBall_choice = choice (eightBall_list)

	# draws the text on the 8ball after it shakes
	eightBall_text = Text(Point(5,5), choice(eightBall_list))
	eightBall_text.setFill('white')
	eightBall_text.draw(windowScreen)
	sleep(.20)

	quitMessage = Text(Point(5,9.5), ("Click anywhere to re-run or click the x to close."))
	quitMessage.setFill('black')
	quitMessage.draw(windowScreen)
	sleep(.20)
		
	windowScreen.getMouse()
	windowScreen.close()		
	return eightBall_list, eightBall_choice, eightBall_text, quitMessage

def main():
	#gives a window with a name and resolution
	windowScreen = GraphWin("Magic 8ball", 500,500)
	#sets the coordinates of the graph
	windowScreen.setCoords(0,0, 10,10)
	#draws a blue circle with a black outline
	circle = Circle(Point(5, 5), 3)
	circle.setFill('blue')
	circle.setOutline('black')
	circle.setWidth(100)
	circle.draw(windowScreen)
	# makes the circle move up and down 4 times
	for i in range (4):
		circle.move(0,.20)
		sleep(.15)
		circle.move(0,-.20)
		sleep(.15)
		circle.move(0,0)
		sleep(.15)
	
	#calls the run function	
	eightBall_list, eightBall_choice, eightBall_text, quitMessage = run(windowScreen, circle)
	main2 = main()
	#loops the program if you click inside the graphical window
	while main() != False:
		main2
		
main()
