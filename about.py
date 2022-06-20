
import pygame, sys

def ABOUT(screen) :

	pygame.init()


	background = pygame.image.load("my.png") 

	window = True

	back = pygame.image.load("Back.png")

	sudoku = pygame.image.load("sudoku.png")

	x = 320 

	y = 100

	font = pygame.font.Font("font.ttf",50)

	font1 = pygame.font.Font("text.ttf",12)

	font2 = pygame.font.Font("font.ttf",35)

	X = 250

	Y = 30

	def ins() :

		text = font.render("SUDOKU",True,(0,255,0))
	
		info = font1.render("Sudoku is a logic-based,number-placement puzzle. ",True,(255,255,0))

		info1 = font1.render("The objective is to fill a 9*9 grid with digits so  ",True,(255,255,0))

		info2 = font1.render("that each column , each row and each of the nine 3*3 ",True,(255,255,0))

		info3 = font1.render("subgrids that compose the grid contain all the digits",True,(255,255,0))

		info4 = font1.render("from 1 to 9 in a given partially complrted grid.",True,(255,255,0))

		info5 = font2.render(" ABOUT THE GUI ",True,(0,255,0))

		info6 = font1.render("This game provides you two features i.e Solve and Play .",True,(255,255,0))

		info7 = font1.render("By clicking on 'solve' button an empty grid is opened , you can fill the grid and create  ",True,(255,255,0) )

		info8 = font1.render("your own sudoku then click solve - immediately solved sudoku will be displayed. ",True,(255,255,0))

		info9 = font1.render("By clicking on the play button you can choose the level of difficulty o the puzzle - Easy/",True,(255,255,0))

		info10 = font1.render(" Medium/Hard - and you can start solving the sudoku displayed with a timer.",True,(255,255,0))

		screen.blit(info9,(10,470))

		screen.blit(info10,(10,490))		

		screen.blit(info8,(10,430))

		screen.blit(info7,(10,410))

		screen.blit(info6,(10,370))		

		screen.blit(info5,(10,320))
		
		screen.blit(info2,(10,180))

		screen.blit(info3,(10,200))

		screen.blit(info4,(10,220))
			
		screen.blit(info1,(10,160))

		screen.blit(info,(10,120))		

		screen.blit(text,(X,Y))		
 
	def example() :

		screen.blit(sudoku,(x,y))

		screen.blit(back,(12,540))
	
	while True :

		screen.blit(background,(0,0))

		ins()

		example()

		for event in pygame.event.get() :

			if event.type == pygame.QUIT :

				pygame.quit()
				sys.exit()

			elif event.type == pygame.MOUSEBUTTONDOWN :

				x, y = pygame.mouse.get_pos()

				if x > 12 and x < 60 and y > 540 and y < 588 :
					screen.fill((255,255,255))
					return


 
		pygame.display.update()
	
		




