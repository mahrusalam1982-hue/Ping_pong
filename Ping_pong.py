from pygame import *
import sys
import random

# ---------- SETTINGS ----------
win_width = 600
win_height = 500
FPS = 60
back = (200, 255, 255)

# ---------- INIT ----------
init()
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
clock = time.Clock()

# ---------- CLASSES ----------
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# ---------- OBJECTS ----------
racket1 = Player('C:\\Users\\LENOVO\\OneDrive\\Desktop\\Pong\\racket.png', 30, 200, 5, 20, 100)
racket2 = Player('C:\\Users\\LENOVO\\OneDrive\\Desktop\\Pong\\racket.png', 550, 200, 5, 20, 100)
ball = GameSprite('C:\\Users\\LENOVO\\OneDrive\\Desktop\\Pong\\ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font = font.Font(None, 35)
lose1 = font.render('Player 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('Player 2 LOSE!', True, (180, 0, 0))

game = True
finish = False

# ---------- GAME LOOP ----------
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Wall collision
        if ball.rect.y <= 0 or ball.rect.y >= win_height - 50:
            speed_y *= -1

        # Paddle collision
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        # Losing conditions
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
