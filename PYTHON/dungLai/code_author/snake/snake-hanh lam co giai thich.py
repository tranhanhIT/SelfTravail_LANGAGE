import pygame
from time import sleep
from random import randint

pygame.init()
screen = pygame.display.set_mode((601, 601)) # chuyển lên 1 đơn vị cho các ô kẻ vuông góc đẹp
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 250, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
clock = pygame.time.Clock()

# x, y là tọa độ của mỗi con rắn: snake position
# snake = [19,19] # ô vuông nằm tọa độ 600,600 muốn có nhiều điểm phải tạo danh sách
#tail - head : trong list cũng vậy, giá trị đầu tiên là đuôi, 2 là đầu
# snakes = [[5,6],[5,7][5,8]]
snakes = [[5,10]] # để lúc ban đầu vừa vào của con rắn chỉ có 1 ô vuông
direction = "right"

apple = [randint(0,19),randint(0,19)]
font_small =pygame.font.SysFont('sans',20) # hiện chữ ghi điểm 
font_big = pygame.font.SysFont('sans',50) # cho chữ hiện ra Game over
score = 0 # khởi tạo biến điểm ban đầu là 0

# Làm dừng con rắn lại, khởi tạo cho pausing = false: vừa vào chương trình khởi tạo là false nghĩa là chương trình sẽ chạy luôn không dừng lại
# Nếu dừng lại là True nhưng khi con rắn chạm vào cạnh thì dừng lại đổi pausing = True, thì rắn sẽ không di chuyển nữa

pausing = False # kho
while running:		
	clock.tick(60)
	screen.fill(BLACK)

	#Tạo 1 copy mới để thêm điểm vào đuôi con rắn: nghĩa là thêm 1 cặp giá trị vào đầu list
	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	#Draw grid
	for i in range(21):
		pygame.draw.line(screen,WHITE,(0,i*30),(600,i*30)) # vẽ đường kẻ ngang
		pygame.draw.line(screen,WHITE,(i*30,0),(i*30,600)) # vẽ đường kẻ dọc

	#Draw snake:
	for snake in snakes:
		pygame.draw.rect(screen,GREEN,(snake[0]*30,snake[1]*30,30,30)) # 30 30 là để lấp đầy hình vuông con rắn

	#Draw apple
	pygame.draw.rect(screen,RED,(apple[0]*30,apple[1]*30,30,30))

	#point
	if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
		snakes.insert(0,[tail_x,tail_y])
		apple = [randint(0,19),randint(0,19)]
		score += 1
	
	# Làm quả táo ngẫu nhiên ngay bên trên lưng con rắn khi đã ăn đc mồi.
	# Tiếng anh gọi trường hợp này là edge case: tìm hiểu thêm
	for snake in snakes:
		while (apple != abc:	
			apple = [randint(0,19),randint(0,19)]
	# Check crash with edge: kiểm tra nếu con rắn chạm vào các cạnh sẽ thua
	if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
		pausing = True
	

	# Draw score: ghi điểm bên góc trái màn hình
	score_txt = font_small.render("Score : " + str(score),True,WHITE)
	screen.blit(score_txt,(5,5))
	#Snake moves
	if pausing == False: # pausing = False thi các lệnh bên dưới chạy còn bằng True sẽ dừng lại
		if direction == "right":
			snakes.append([snakes[-1][0]+1,snakes[-1][1]])
			snakes.pop(0)
		if direction == "left":
			snakes.append([snakes[-1][0]-1,snakes[-1][1]])
			snakes.pop(0)
		if direction == "up":
			snakes.append([snakes[-1][0],snakes[-1][1]-1])
			snakes.pop(0)
		if direction == "down":
			snakes.append([snakes[-1][0],snakes[-1][1]+1])
			snakes.pop(0)
	# Check crash with body
	for i in range(len(snakes)-1):
		if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
			pausing = True

	# Draw game over
	if pausing:
		game_over_txt = font_big.render("Game over, score: " + str(score), True, WHITE) # True: làm cho chữ mượt
		press_space_txt = font_big.render("Press Space to continue ", True, WHITE)
		screen.blit(game_over_txt,(50,200)) #50,200: in ra giữa màn hình 
		screen.blit(press_space_txt,(50,300))

	sleep(0.1) # để cho snake di chuyển chậm lại or dừng màn hình


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"
			if event.key == pygame.K_SPACE and pausing == True:
				pausing = Falses 
				snakes = [[5,10]]
				apple = [randint(0,19),randint(0,19)]
				score = 0
 	
 	pygame.display.flip()

pygame.quit()

"""
search key: pygame key code sẽ ra danh sách những phím tương ứng
snakes.append([snakes[-1][0],snakes[-1][1]-1]): 
append: thêm vào danh sách
snakes[-1]: nghĩa là luôn luôn lấy cặp cuối của danh sách snakes
		[0]: lấy giá trị đầu tiên của cặp danh sách
		[1]: lấy phần tử thứ 2

edge case: trường hợp đặc biệt
"""