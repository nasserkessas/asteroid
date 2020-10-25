from random import randint, uniform

WIDTH = 800
HEIGHT = 600

SHIP_SPEED = 4
game_over = False
game_over_frame = 0
spaceship = Actor("spaceship")
spaceship.pos = (WIDTH / 2, HEIGHT - 55)

KEYS = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
}

def make_star(y=None):
    size = randint(1,3)
    stars.append({"x": randint(0, WIDTH), "y": y if y != None else randint(0, HEIGHT), "width": size, "shade": 127 + size * 32})

def start():
    global game_over, game_over_frame, spaceship
    STAR_COUNT = 50
    ASTEROID_COUNT = 5
    game_over = False
    game_over_frame = 0

    spaceship = Actor("spaceship")
    spaceship.pos = (WIDTH / 2, HEIGHT - 55)
    global stars, asteroids

    stars = []
    asteroids = []



    for i in range(STAR_COUNT):
        make_star()

    for i in range(ASTEROID_COUNT):
        asteroids.append({
        "actor": Actor("asteroid_" + str(randint(1, 5))),
        "rotation_speed": uniform(0.3, 2),
        "speed": uniform(1, 3)
        })

    for asteroid in asteroids:
        asteroid["actor"].pos = (randint(0, WIDTH), 0)

start()

def draw():
    global game_over_frame
    screen.clear()
    screen.fill((15, 4, 30))

    for star in stars:
        screen.draw.filled_circle((star["x"], star["y"]), star["width"], (star["shade"], star["shade"], star["shade"]))
    for asteroid in asteroids:
        asteroid["actor"].draw()
    if game_over_frame < 4:
        spaceship.draw()

    if game_over:
        if game_over_frame >= 0 and game_over_frame < 1:
            spaceship.image = "explosion_1"
        if game_over_frame >= 1 and game_over_frame < 2:
            spaceship.image = "explosion_2"
        if game_over_frame >= 2 and game_over_frame < 3:
            spaceship.image = "explosion_3"
        if game_over_frame>4:
            screen.draw.text("GAME OVER", color = "white", center=(WIDTH/2,HEIGHT/2), fontsize=80)
            screen.draw.text("Press ENTER to play again", color = "white", center=(WIDTH/2,HEIGHT/2+50), fontsize=35)
        game_over_frame += 0.4



def update():
    global game_over
    if game_over_frame < 4:
        for star in stars:
            star["y"] += 0.5
            if star["y"] > HEIGHT:
                stars.remove(star)
                make_star(0)

        for asteroid in asteroids:
            actor = asteroid["actor"]
            actor.bottom += asteroid["speed"]
            if actor.bottom > HEIGHT:
                asteroids.remove(asteroid)
                asteroids.append({"actor": Actor("asteroid_" + str(randint(1, 5))), "rotation_speed": uniform(0.3, 2), "speed": uniform(1, 3)})
                asteroids[len(asteroids)-1]["actor"].pos = (randint(0, WIDTH), 0)
            actor.angle += asteroid["rotation_speed"]


        if KEYS["left"] and spaceship.left > 0:
            spaceship.left -= SHIP_SPEED
        if KEYS["right"] and spaceship.right < WIDTH:
            spaceship.left += SHIP_SPEED
        if KEYS["up"] and spaceship.top > 0:
            spaceship.top -= SHIP_SPEED
        if KEYS["down"] and spaceship.bottom < HEIGHT:
            spaceship.top += SHIP_SPEED


    for asteroid in asteroids:
        touching = spaceship.colliderect(asteroid["actor"])
        if touching:
            game_over = True



def on_key_down(key):
    global KEYS
    if key == keys.RIGHT:
        KEYS["right"] = True
    if key == keys.LEFT:
        KEYS["left"] = True
    if key == keys.UP:
        KEYS["up"] = True
    if key == keys.DOWN:
        KEYS["down"] = True

    if game_over_frame > 4 and key == keys.RETURN:
        start()

def on_key_up(key):
    global KEYS
    if key == keys.RIGHT:
        KEYS["right"] = False
    if key == keys.LEFT:
        KEYS["left"] = False
    if key == keys.UP:
        KEYS["up"] = False
    if key == keys.DOWN:
        KEYS["down"] = False



'''
asteroid = []
def generate():
    global asteroid
    verticies = randint(10, 20)
    center = {"x": randint(0, WIDTH), "y": randint(0, HEIGHT)}
    for i in range(verticies):
        distance = randint(30, 50)
        deg = randint(1, 360)
        asteroid.append({"distance": distance, "degrees": deg, "x": center["x"] + distance / sin(deg * pi / 180), "y": center["y"] + distance / cos(deg * pi / 180)})
    print(str(asteroid), "length: ", str(len(asteroid)))

generate()

def draw():
    global asteroid
    screen.clear()
    screen.fill((21, 8, 54))
    for i in range(len(asteroid)):
        screen.draw.line((asteroid[i]["x"], asteroid[i]["y"]), (asteroid[i+1 if (i+1) < len(asteroid) else 0]["x"], asteroid[i+1 if (i+1) < len(asteroid) else 0]["y"]), (100, 100, 100))
'''