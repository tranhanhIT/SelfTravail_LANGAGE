import pygame
from random import randint
pygame.init()
WIDTH, HEIGHT = 400,600 # 400: chiều rộng màn hình, 600: chiều cao màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Flappy Bird')
running = True

GREEN = (0, 200, 0)
BLUE = (0,0,255)
RED = (255,0,0) # màu đỏ của con chim
BLACK = (0,0,0) # 255,255,255 : màu trắng

clock = pygame.time.Clock()
# sử dụng chữ in hoa là biến constant: hằng không đổi
TUBE_WIDTH = 50
TUBE_VELOCITY = 3 # tốc độ đi sang trái
TUBE_GAP = 150

tube1_x = 600  # cho ống bắt đầu xuất hiện từ phía phải màn hình
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

BIRD_X = 50
bird_y = 400 # viết thường vì nó thay đổi
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans',20) 

tube1_pass = False # vì nó chưa đi qua thì cho bằng false qua rồi là bằng true
tube2_pass = False
tube3_pass = False

pausing = False # tạo biến khi màn hình đang dừng lại để reset lại mọi thứ về 0
while running:		
	clock.tick(60)
	screen.fill(GREEN)

	#Draw tube
	#tính tọa độ chạm của con chim nên phải cho tube1_rect = cả pygame...lúc nào cũng có 6 hình chữ nhật; 3 trên và 3 dưới
	tube1_rect = pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WIDTH,tube1_height)) # 0: là từ gốc tọa độ trục tung và trục hoành
	#tube1_x = tube1_x - 3 # di chuyển ống từ phải sang trái,kinh nghiệm khi code không sử dụng con số trong code gọi là hard code mà phải sử dụng như dưới
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
	#pygame.draw.rect(screen,RED,(truyền vào 4 con số))
	bird_rect = pygame.draw.rect(screen,RED,(BIRD_X,bird_y,BIRD_WIDTH,BIRD_HEIGHT))

	#bird falls
	bird_y += bird_drop_velocity # muốn đi lên thì - 
	bird_drop_velocity += GRAVITY

	# tạo ống mới chạy ống và khoảng cách(generate new tubes)
	if tube1_x <-TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100,400) # khi tạo ống mới phải randint lại
		tube1_pass = False # tạo lại ống mới chưa tính điểm cho nó
	if tube2_x <-TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(100,400)
		tube2_pass = False
	if tube3_x <-TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100,400)
		tube3_pass = False

	# in ra màn hình :tạo font chữ trên while và tạo chữ rồi in ra màn hình
	score_txt = font.render("Score: " + str(score),True, BLACK) # phải đổi từ số sang string mới in ra text đc; True: làm cho chữ mượt in ra, Black: màu chữ
	screen.blit(score_txt,(5,5)) # blit: vẽ lên màn hình (5,5): ngay phần trên, tọa độ của nó

	# update score: cộng điểm
	# để ý cộng điểm khi đi qua phải dùng tube_pass = false... Nhưng khi đi hết 3 ống rồi lại phải cho trở về là false ở phần tạo ống line70
	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False: # đi hết cạnh của ống 0 + 50; làm sao để nó không bị cộng điểm nhiều lần khi chưa đi hết 1 ống.
		score += 1 # làm sao chỉ cộng 1 điểm khi và 1 lần khi đi hết ống đó thôi; phải tạo nên 1 biến mới là tube1_pass để kiểm tra xem đã đi qua chưa
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True
	
	#check collision : kiểm tra khi nào con chim chạm vào ống
"""	if bird_rect.colliderect(tube1_rect): # kiểm tra ống 1 xem có chạm vào ống 2 không. bird_rect xem có chạm vào tube1_rect không.
		TUBE_VELOCITY = 0
	if bird_rect.colliderect(tube2_rect):
		TUBE_VELOCITY = 0 # trọng lượng trở về 0
	if bird_rect.colliderect(tube3_rect):
		TUBE_VELOCITY = 0
	# làm tương tự như thế với 3 ống bên dưới. tuy nhiên có cách dùng vòng lặp for ngắn gọn hơn như sau     		"""
    for tube in [tube1_rect, tube2_rect, tube3_rect, tube1_rect_inv, tube2_rect_inv, tube3_rect_inv]:
		if bird_rect.colliderect(tube):
			pausing = True # khi các ống chạm vào nhau thì thành true
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0 # dừng con chim 
			game_over_txt = font.render("Game over, score: "+str(score),True,BLACK)
			screen.blit(game_over_txt,(200,300)) # vẽ chữ lên màn hình...
			press_space_txt = font.render("Press Space to Continue ",True,BLACK)
			screen.blit(press_space_txt,(200,400))


	for event in pygame.event.get():  # event là những nút chuột bấm vào
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN: # check khi nào ấn nút trên bàn phím
			if event.key == pygame.K_SPACE: # check khi nào ấn nút cách
				#reset lại các sự kiện
				if pausing:
					bird_y = 400
					TUBE_VELOCITY = 3
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					score = 0
					pausing = False # để cho hàm if pausing chỉ đc chạy đúng 1 lần khi ấn nút cách
				
				
				bird_drop_velocity = 0 # khi ấn nút cách nó sẽ về 0- reset lại nút rơi tự do về 0
				bird_drop_velocity -= 10 # làm cho con chim đi lên, vận tốc sẽ đảo ngược lên và gavity vẫn bị trừ đi 

	pygame.display.flip()

pygame.quit()