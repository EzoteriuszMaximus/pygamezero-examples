player = Actor("temporary_player")
player.topright = 150, 10

WIDTH = 300
HEIGHT = player.height + 20

def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    player.draw()

def update():
    player.left += 2
    if player.left > WIDTH:
        player.right = 0

def on_mouse_down(pos, button):
    if player.collidepoint(pos) and button == mouse.LEFT:
        set_player_hurt()
        clock.schedule_unique(set_player_normal, 1.0)

def set_player_hurt():
  player.image = "temporary_player_hurt"
  sounds.temp_hurt.play()

def set_player_normal():
  player.image = "temporary_player"