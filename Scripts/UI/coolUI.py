# requires: pip install asciimatics
# tutorials from: 
# https://github.com/peterbrittain/asciimatics
# https://ludusrusso.cc/2018/04/04/python-scrivere-terminal-gui/
#
# Docs: http://asciimatics.readthedocs.io/en/stable/


from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from random import randint


def demo_stars(screen): 
	#effects is an array that contains the effects we want to apply to our UI
	#2 Cycle Effects and 1 Stars
	
	effects = [
		#Cycle let cycle the color of the text we are passing it
		Cycle(
			screen,
			FigletText("Rensykes", font='big'), #you can use other Figlet 
			int(screen.height / 2 - 8)),
		Cycle(
			screen,
			FigletText("Learn asciimatics!", font='small'),
			int(screen.height / 2 + 3)),
		Stars(screen, 500) #draw a certain ammpunt of stars
	]
	screen.play([Scene(effects, 500)]) #renderize the scene with the effects 
	ev = screen.get_key() #use it to get the key pressed
	if ev in (ord('Q'), ord('q')):
		return
	screen.refresh()

def demo_helloWorld(screen):
	while True:
		screen.print_at('Hello world!',
					randint(0, screen.width), randint(0, screen.height),
					colour=randint(0, screen.colours - 1),
					bg=randint(0, screen.colours - 1))
		ev = screen.get_key()
		if ev in (ord('Q'), ord('q')):
			 return
		screen.refresh()

Screen.wrapper(demo_helloWorld)