import pygame

pygame.init()
screen = pygame.display.set_mode((601, 601)) # chuyển lên 1 đơn vị cho các ô kẻ vuông góc đẹp
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 250, 0)
BLACK = (0,0,0)
WHITE = (255,255,255)
clock = pygame.time.Clock()

# x, y là tọa độ của mỗi con rắn: snake position
# snake = [19,19] # ô vuông nằm tọa độ 600,600 muốn có nhiều điểm phải tạo danh sách
#tail - head : trong list cũng vậy, giá trị đầu tiên là đuôi, 2 là đầu
snakes = [[5,6],[5,7]]


while running:		
	clock.tick(60)
	screen.fill(BLACK)

	#Draw grid
	for i in range(21):
		pygame.draw.line(screen,WHITE,(0,i*30),(600,i*30)) # vẽ đường kẻ ngang
		pygame.draw.line(screen,WHITE,(i*30,0),(i*30,600)) # vẽ đường kẻ dọc

	#Draw snake:
	for snake in snakes:
		pygame.draw.rect(screen,GREEN,(snake[0]*30,snake[1]*30,30,30)) # 30 30 là để lấp đầy hình vuông con rắn


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				snake[1] -= 1
			if event.key == pygame.K_DOWN:
				snake[1] += 1
			if event.key == pygame.K_LEFT:
				snake[0] -= 1
			if event.key == pygame.K_RIGHT:
				snake[0] += 1
	pygame.display.flip()

pygame.quit()

"""
search key: pygame key code sẽ ra danh sách những phím tương ứng
"""