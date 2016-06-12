import random,sys,pygame
from time import sleep
from classes import *
pygame.init()
clock = pygame.time.Clock()

#Initializing Things
WIDTH = 130
HEIGHT = 130
SIZE = (1000,700)
INIT_X = 0
INIT_Y = SIZE[1] - HEIGHT
VEL_X = 4
VEL_Y = 6
FPS = 80
bot_frame = 0
jump_state_flag = False
Idle = ["png/Idle (1).png", "png/Idle (2).png", "png/Idle (3).png", "png/Idle (4).png", "png/Idle (5).png", "png/Idle (6).png", "png/Idle (7).png", "png/Idle (8).png", "png/Idle (9).png", "png/Idle (10).png"]
Jump = ["png/Jump (1).png", "png/Jump (2).png", "png/Jump (3).png", "png/Jump (4).png", "png/Jump (5).png", "png/Jump (6).png", "png/Jump (7).png", "png/Jump (8).png", "png/Jump (9).png", "png/Jump (10).png"]
Run = ["png/Run (1).png", "png/Run (2).png", "png/Run (3).png", "png/Run (4).png", "png/Run (5).png", "png/Run (6).png", "png/Run (7).png", "png/Run (8).png"]
Shoot = ["png/Shoot (1).png","png/Shoot (2).png","png/Shoot (3).png","png/Shoot (4).png"]
RunShoot = ["png/RunShoot (1).png", "png/RunShoot (2).png", "png/RunShoot (3).png", "png/RunShoot (4).png", "png/RunShoot (5).png", "png/RunShoot (6).png", "png/RunShoot (7).png", "png/RunShoot (8).png"]

images = [Idle,Jump,Run,Shoot,RunShoot]
bot = Bot(images,INIT_X,INIT_Y,WIDTH,HEIGHT,0,0)
bullet = Bullet(INIT_X,INIT_Y,30,30,"png/FireBall.png")
screen = pygame.display.set_mode(SIZE,0,32)
pygame.display.set_caption('SharpShooter')
COLOR = (255,255,255)

#Game Loop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type== pygame.KEYDOWN:
			if event.key== pygame.K_RIGHT:
				bot.velx = VEL_X
				bot.state=2
				bot.direction = 0
				jump_state_flag = False
			if event.key == pygame.K_LEFT:
				bot.direction = 1
				bot.velx = -VEL_X
				bot.state=2
				jump_state_flag = False
			if event.key == pygame.K_UP and bot.rect.y == INIT_Y:
				bot.vely = -VEL_Y
				bot.state = 1
				jump_state_flag = True
			if event.key == pygame.K_SPACE :
				if bot.velx == 0:
					bot.state = 3
				else :
					bot.state = 4
				Bullet.bullets.add(bullet)
				
				if bot.direction == 0:
					bullet.velx = 2*VEL_X
					bullet.tick(bot.rect.x + bot.rect.width/2,bot.rect.y+bot.rect.height/3,bullet.rect.width,bullet.rect.height)
				else:
					bullet.velx = -2*VEL_X
					bullet.tick(bot.rect.x+bot.rect.width/4,bot.rect.y+bot.rect.height/3,bullet.rect.width,bullet.rect.height)

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				bot.velx = 0
				bot.state = 0
			if event.key == pygame.K_SPACE:
				if bot.velx == 0:
					bot.state = 0
				else :
					bot.state = 2
				

	if(bot.rect.y > INIT_Y):
		bot.vely = 0
		bot.rect.y = INIT_Y 
		if jump_state_flag == True:
			if bot.velx != 0:
				bot.state = 2
			else :
				bot.state = 0
			jump_state_flag = False

	
	bot.update()
	bullet.update()
	bot_frame += 1
	if(bot_frame == FPS/10):
		bot_frame = 0
		bot.tick(bot.rect.x,bot.rect.y,bot.rect.width,bot.rect.height)
	screen.fill(COLOR)	
	Bot.bots.draw(screen)
	Bullet.bullets.draw(screen)
	pygame.display.flip()
	clock.tick(FPS)