import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 400,600 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Flappy Bird')
running = True

GREEN = (0, 200, 0)
BLUE = (0,0,255)
RED = (255,0,0) 
BLACK = (0,0,0) 

clock = pygame.time.Clock()
# sử dụng chữ in hoa là biến constant: hằng không đổi
TUBE_WIDTH = 50
TUBE_VELOCITY = 3 
TUBE_GAP = 150

tube1_x = 600  
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

BIRD_X = 50
bird_y = 400 
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans',20) 

tube1_pass = False 
tube2_pass = False
tube3_pass = False

pausing = False 
while running:		
	clock.tick(60)
	screen.fill(GREEN)

	#Draw tube
	tube1_rect = pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height)) 
	tube2_rect = pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WIDTH,tube2_height))
	tube3_rect = pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WIDTH,tube3_height))
	
	#Draw tube inverse
	h1 = HEIGHT - tube1_height-TUBE_GAP
	h2 = HEIGHT - tube2_height-TUBE_GAP
	h3 = HEIGHT - tube3_height-TUBE_GAP
	#pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height + TUBE_GAP,TUBE_WIDTH, HEIGHT - tube1_height-TUBE_GAP))
	tube1_rect_inv = pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height + TUBE_GAP,TUBE_WIDTH,h1))
	tube2_rect_inv = pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height + TUBE_GAP,TUBE_WIDTH,h2))
	tube3_rect_inv = pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height + TUBE_GAP,TUBE_WIDTH,h3))

	# move tube to the left
	tube1_x = tube1_x - TUBE_VELOCITY # velocity: tốc độ
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	# draw bird
	bird_rect = pygame.draw.rect(screen,RED,(BIRD_X,bird_y,BIRD_WIDTH,BIRD_HEIGHT))

	#bird falls
	bird_y += bird_drop_velocity 
	bird_drop_velocity += GRAVITY

	# tạo ống mới chạy ống và khoảng cách(generate new tubes)
	if tube1_x <-TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100,400) 
		tube1_pass = False 
	if tube2_x <-TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(100,400)
		tube2_pass = False
	if tube3_x <-TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100,400)
		tube3_pass = False

	# in ra màn hình :tạo font chữ trên while và tạo chữ rồi in ra màn hình
	score_txt = font.render("Score: " + str(score),True, BLACK) 
	screen.blit(score_txt,(5,5)) 

	# update score: cộng điểm
	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False: 
		score += 1 
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True
	
	#check collision : kiểm tra khi nào con chim chạm vào ống
for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv]:
		if bird_rect.colliderect(tube):
			pausing = True 
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0 
			game_over_txt = font.render("Game over, score: " + str(score),True,BLACK)
			screen.blit(game_over_txt,(200,300)) 
			press_space_txt = font.render("Press Space to Continue ",True,BLACK)
			screen.blit(press_space_txt,(200,400))


for event in pygame.event.get():  
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_SPACE: 
				#reset lại các sự kiện
				if pausing:
					bird_y = 400
					TUBE_VELOCITY = 3
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					score = 0
					pausing = False 
					bird_drop_velocity = 0 
					bird_drop_velocity -= 10 
pygame.display.flip()

pygame.quit()