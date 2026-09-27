import kandinsky
import time
import ion
import math
import random


SCREEN_WIDTH = 320
SCREEN_HEIGHT = 222

FPS = 30

APR = 1
STEP_SIZE = 1

SHADE_CORRECTION = 25

GUN_RANGE = 3

# === Data Types ===

class LocalMapTiles(): #{
    VOID = 0
    SPAWN = 1
    WALL_TYPE_0 = 2
    WALL_TYPE_1 = 3
    MONSTER = 4
#}

MAP_TILES = LocalMapTiles()
MAP_TILE_COLORS = [
    [0, 0, 0],
    [0, 0, 0],
    [152, 157, 158],
    [245, 197, 66],
    [6969, 6969, 6969]
]

class LocalRectangle: #{
    x = 0
    y = 0
    w = 0
    h = 0
    color = kandinsky.color(0, 0 ,0)
#}

class LocalText: #{
    x = 0
    y = 0
    text = "NULL"
    foreground = kandinsky.color(0, 0, 0)
    background = kandinsky.color(255, 255, 255)
#}

class LocalPlayer: #{
    x = 0
    y = 0
    fov = 0
    angle = 0
    render_distance = 0
    move_speed = 0.0
    turn_speed = 0
    points = 0
    health = 100
#}

class LocalMap: #{
    map = []
    map_width = 0
    map_height = 110
#}

class LocalRay: #{
    x = 0
    width = 0
    height = 0
    distance = 0
    visible = False
    color = [0, 0, 0]
#}

class LocalMonster: #{
    prex = 0
    prey = 0
    x = 0
    y = 0
    damage = 10
#}

# === Main Block ===

def main(): #{
    if title_screen(): #{
        map = LocalMap()
        map.map = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2],
            [2, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0, 2],
            [2, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2]
        ]

        map.map_height = len(map.map)
        map.map_width = len(map.map[0])

        player = LocalPlayer()
        player.angle = 0
        player.fov = 80
        player.render_distance = 20
        player.move_speed = 0.5
        player.turn_speed = 5
        player.health = 100

        ray_caster(map, player, kandinsky.color(110, 207, 255), kandinsky.color(49, 94, 52))
        
        exit_screen(player.points)

    #}
#}

def title_screen(): #{

    title = LocalText()
    title.text = "Raycaster"
    title.x = SCREEN_WIDTH // 2 - 10 * 5
    title.y = 40
    title.foreground = kandinsky.color(255, 255, 255)
    title.background = kandinsky.color(0, 0, 0)

    button = LocalRectangle()
    button.h = 20
    button.w = 40
    button.x = SCREEN_WIDTH // 2 - button.w
    button.y = SCREEN_HEIGHT // 2 + 10 - button.h
    button.color = kandinsky.color(110, 110, 110)

    play = LocalText()
    play.text = "Press OK"
    play.x = button.x
    play.y = button.y
    play.foreground = kandinsky.color(255, 255, 255)
    play.background = button.color

    while True: #{
        clear_screen(kandinsky.color(0, 0, 0))
        
        render_text(title)
        render_rectangle(button)
        render_text(play)

        if ion.keydown(ion.KEY_BACK): #{
            return False
        #}
        elif ion.keydown(ion.KEY_OK): #{
            return True
        #}

        time.sleep(1/FPS)
    #}
#}

def exit_screen(points): #{

    time.sleep(1)

    title = LocalText()
    title.text = "Points: " + str(points)
    title.x = SCREEN_WIDTH // 2 - 10 * 5
    title.y = 40
    title.foreground = kandinsky.color(255, 255, 255)
    title.background = kandinsky.color(0, 0, 0)

    while True: #{
        clear_screen(kandinsky.color(0, 0, 0))
        
        render_text(title)

        if ion.keydown(ion.KEY_BACK): #{
            break
        #}
        time.sleep(1/FPS)
    #}
#}

def ray_caster(map, player, sky_color, floor_color): #{
   
    for y in range(map.map_height): #{
        for x in range(map.map_width): #{
            if map.map[y][x] == MAP_TILES.SPAWN: #{
                player.x = x
                player.y = y
            #}
        #}
    #}

    sky = LocalRectangle()
    sky.x = 0
    sky.y = 0
    sky.w = SCREEN_WIDTH
    sky.h = SCREEN_HEIGHT // 2
    sky.color = sky_color

    floor = LocalRectangle()
    floor.x = 0
    floor.w = SCREEN_WIDTH
    floor.h = SCREEN_HEIGHT // 2
    floor.y = SCREEN_HEIGHT - floor.h
    floor.color = floor_color

    gun = LocalPlayer()
    gun.fov = 5
    gun.angle = player.angle
    gun.x = player.x
    gun.y = player.y
    gun.render_distance = GUN_RANGE

    monster = LocalMonster()
    while True: #{
        mx = random.randint(0, map.map_width - 1)
        my = random.randint(0, map.map_height - 1)

        if map.map[my][mx] == MAP_TILES.VOID or map.map[my][mx] == MAP_TILES.SPAWN: #{
            if mx != player.x or my != player.y: #{
                monster.x = mx
                monster.prex = mx
                monster.y = my
                monster.prey = my
                break
            #}
        #}
    #}
    map.map[monster.y][monster.x] = MAP_TILES.MONSTER
    monster.damage = 10

    monster_on_player = False


    while True: #{

        gun.angle = player.angle
        gun.x = player.x
        gun.y = player.y

        if monster.x == player.x and monster.y == player.y: monster_on_player = True
        else: monster_on_player = False

        ray_count = round(player.fov / APR)
        ray_width = round(max(1, SCREEN_WIDTH / ray_count))

        clear_screen(kandinsky.color(0, 0, 0))

        render_rectangle(sky)

        render_rectangle(floor)

        rays = get_rays(map, player, ray_count, ray_width)
        render_rays(rays)

        draw_gun(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT - 60, 30, 60, False)
        
        if ion.keydown(ion.KEY_BACK): #{
            break
        #}
        elif ion.keydown(ion.KEY_UP): #{
            next_y = player.y + math.cos(math.radians(player.angle)) * player.move_speed
            next_x = player.x + math.sin(math.radians(player.angle)) * player.move_speed

            next_y = min(map.map_height - 1, next_y)
            next_x = min(map.map_width - 1, next_x)
            next_x = max(0, next_x)
            next_y = max(0, next_y)

            if map.map[round(next_y)][round(next_x)] == MAP_TILES.VOID or map.map[round(next_y)][round(next_x)] == MAP_TILES.SPAWN: #{
                player.x = next_x
                player.y = next_y
            #}
        #}
        elif ion.keydown(ion.KEY_DOWN): #{
            next_y = player.y - math.cos(math.radians(player.angle)) * player.move_speed
            next_x = player.x - math.sin(math.radians(player.angle)) * player.move_speed

            next_y = min(map.map_height - 1, next_y)
            next_x = min(map.map_width - 1, next_x)
            next_x = max(0, next_x)
            next_y = max(0, next_y)

            if map.map[round(next_y)][round(next_x)] == MAP_TILES.VOID or map.map[round(next_y)][round(next_x)] == MAP_TILES.SPAWN: #{
                player.x = next_x
                player.y = next_y
            #}
        #}
        elif ion.keydown(ion.KEY_LEFT): #{
            player.angle -= player.turn_speed
            if player.angle < 0: player.angle += 360
        #}
        elif ion.keydown(ion.KEY_RIGHT): #{
            player.angle += player.turn_speed
            if player.angle > 360: player.angle -= 360
        #}
        elif ion.keydown(ion.KEY_PLUS): #{
            player.render_distance += 1
            if player.render_distance > max(map.map_height, map.map_width): player.render_distance = max(map.map_height, map.map_width)
        #}
        elif ion.keydown(ion.KEY_MINUS): #{
            player.render_distance -= 1
            if player.render_distance <= 0: player.render_distance = 1
        #}
        elif ion.keydown(ion.KEY_OK): #{
            draw_gun(SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT - 60, 30, 60, True)
            gun_rays = get_rays(map, gun, round(gun.fov / APR), round(max(1, SCREEN_WIDTH / round(gun.fov / APR))))
            hit_monster = False
            for i in range(len(gun_rays)): #{
                if hit_monster: break
                if gun_rays[i].color[0] == 6969: #{
                    hit_monster = True
                    player.points += 1
                    map.map[monster.y][monster.x] = MAP_TILES.VOID
                    while True: #{
                        mx = random.randint(0, map.map_width - 1)
                        my = random.randint(0, map.map_height - 1)

                        if map.map[my][mx] == MAP_TILES.VOID or map.map[my][mx] == MAP_TILES.SPAWN: #{
                            if mx != player.x or my != player.y: #{
                                if mx != monster.prex or my != monster.prey: #{
                                    monster.x = mx
                                    monster.prex = mx
                                    monster.y = my
                                    monster.prey = my
                                    break
                                #}
                            #}
                        #}
                    #}
                    map.map[monster.y][monster.x] = MAP_TILES.MONSTER
                #}
            #}
        #}

        # monster random walk
        if not monster_on_player: #{
            direction = random.randint(0, 80)
            my = monster.y
            mx = monster.x
            if direction == 0: my = monster.y - 1
            elif direction == 1: my = monster.y - 1; mx = monster.x + 1
            elif direction == 2: mx = monster.x + 1
            elif direction == 3: my = monster.y + 1; mx = monster.x + 1
            elif direction == 4: my = monster.y + 1
            elif direction == 5: my = monster.y + 1; mx = monster.x - 1
            elif direction == 6: mx = monster.x - 1
            elif direction == 7: my = monster.y - 1; mx = monster.x - 1
           
            my = min(map.map_height - 1, my)
            mx = min(map.map_width - 1, mx)
            mx = max(0, mx)
            my = max(0, my)

            if map.map[my][mx] == MAP_TILES.VOID or map.map[my][mx] == MAP_TILES.SPAWN and not (monster.x == player.x and monster.y == player.y): #{
                monster.prex = monster.x
                monster.prey = monster.y
                monster.y = my
                monster.x = mx
                map.map[monster.prey][monster.prex] = MAP_TILES.VOID
                map.map[monster.y][monster.x] = MAP_TILES.MONSTER
                
                if math.sqrt(math.pow(monster.x - player.x, 2) + math.pow(monster.y - player.y, 2)) <= 1: #{
                    monster_on_player = True
                #}

            #}
        #}

        if monster_on_player: player.health -= monster.damage; draw_hurt()

        if player.health <= 0: break

        render_info(player)
            
        time.sleep(1/FPS)
    #}
#}

def render_info(player): #{
    kandinsky.draw_string("points: " + str(player.points), 0, SCREEN_HEIGHT - round(SCREEN_HEIGHT * 10/100), kandinsky.color(255, 255, 255), kandinsky.color(0, 0, 0))
    kandinsky.draw_string("health: " + str(player.health), SCREEN_WIDTH - 120, SCREEN_HEIGHT - round(SCREEN_HEIGHT * 10/100), kandinsky.color(255, 255, 255), kandinsky.color(0, 0, 0))
#}

def get_rays(map, player, ray_count, ray_width): #{
   
    rays = []

    for i in range(ray_count): #{
        rays.append(LocalRay())
        rays[i].width = ray_width
    #}

    found_monster = False
    
    for i in range(ray_count): #{
        rays[i].x = i*ray_width
        ray_angle = math.radians(player.angle - player.fov / 2 + i * (player.fov / ray_count))

        steps = 0
        while True: #{
            if steps > player.render_distance: #{
                break
            #}

            steps += 1
            map_y = round(player.y + math.cos(ray_angle) * steps * STEP_SIZE)
            map_x = round(player.x + math.sin(ray_angle) * steps *  STEP_SIZE)
            
            if map_x >= map.map_width: map_x = map.map_width - 1
            if map_x < 0: map_x = 0
            if map_y >= map.map_height: map_y = map.map_height - 1
            if map_y < 0: map_y = 0

            tile = map.map[map_y][map_x]

            if tile != MAP_TILES.SPAWN and tile != MAP_TILES.VOID: #{
                rays[i].distance = steps * STEP_SIZE
                rays[i].visible = True

                
                if tile == MAP_TILES.WALL_TYPE_0: #{
                    rays[i].color = MAP_TILE_COLORS[MAP_TILES.WALL_TYPE_0]
                #}
                elif tile == MAP_TILES.WALL_TYPE_1: #{
                    rays[i].color = MAP_TILE_COLORS[MAP_TILES.WALL_TYPE_1]
                #}
                elif tile == MAP_TILES.MONSTER: #{
                    if not found_monster: #{
                        rays[i].color = MAP_TILE_COLORS[MAP_TILES.MONSTER]
                        found_monster = True
                    #}
                    else: #{
                        while True: #{
                            if steps > player.render_distance: #{
                                break
                            #}

                            steps += 1
                            map_y = round(player.y + math.cos(ray_angle) * steps * STEP_SIZE)
                            map_x = round(player.x + math.sin(ray_angle) * steps *  STEP_SIZE)
            
                            if map_x >= map.map_width: map_x = map.map_width - 1
                            if map_x < 0: map_x = 0
                            if map_y >= map.map_height: map_y = map.map_height - 1
                            if map_y < 0: map_y = 0

                            tile = map.map[map_y][map_x]

                            if tile != MAP_TILES.SPAWN and tile != MAP_TILES.VOID: #{
                                rays[i].distance = steps * STEP_SIZE
                                rays[i].visible = True

                
                                if tile == MAP_TILES.WALL_TYPE_0: #{
                                    rays[i].color = MAP_TILE_COLORS[MAP_TILES.WALL_TYPE_0]
                                #}
                                elif tile == MAP_TILES.WALL_TYPE_1: #{
                                    rays[i].color = MAP_TILE_COLORS[MAP_TILES.WALL_TYPE_1]
                                #}
                                break
                            #}
                        #}
                    #}
                #}
                break
            #}
        #}
    #}

    for i in range(ray_count): #{
        rays[i].height = min(SCREEN_HEIGHT, SCREEN_HEIGHT // (rays[i].distance + 1))
    #}
    
    return rays
#}

def render_rays(rays): #{

    rendered_monster = False
    monster_index = 0
    
    for i in range(len(rays)): #{
        if rays[i].visible: #{
            if rays[i].color[0] != 6969: #{
                line = LocalRectangle()
                line.x = rays[i].x
                line.y = SCREEN_HEIGHT // 2 - rays[i].height // 2
                line.w = rays[i].width
                line.h = rays[i].height
                r = rays[i].color[0] // (rays[i].distance + 1) + SHADE_CORRECTION
                g = rays[i].color[1] // (rays[i].distance + 1) + SHADE_CORRECTION
                b = rays[i].color[2] // (rays[i].distance + 1) + SHADE_CORRECTION
            
                r = max(r, 0)
                r = min(r, 255)
                g = max(g, 0)
                g = min(g, 255)
                b = max(b, 0)
                b = min(b, 255)

                line.color = kandinsky.color(r, g, b)
            
                render_rectangle(line)
            #}
            else: #{
                if not rendered_monster: #{
                    monster_index = i
                    rendered_monster = True
                #}
            #}
        #}
    #}
    if rendered_monster: draw_monster(rays[monster_index].distance, rays[monster_index].x)
#}

def draw_gun(x, y, w, h, fired): #{
    #hand
    hand_c = kandinsky.color(255, 224, 133)
    hand_h = 40 * h / 100
    hand_y = y + h - hand_h
    hand_w = w
    hand_x = x
    kandinsky.fill_rect(round(hand_x), round(hand_y), round(hand_w), round(hand_h), hand_c)
    #gun_barrel
    gun_barrel_c = kandinsky.color(56, 56, 56)
    gun_barrel_h = h * (60 / 100)
    gun_barrel_y = hand_y - gun_barrel_h * (50 / 100)
    gun_barrel_w = w * (50 / 100)
    gun_barrel_x = x + hand_w / 4
    kandinsky.fill_rect(round(gun_barrel_x), round(gun_barrel_y), round(gun_barrel_w), round(gun_barrel_h), gun_barrel_c)
    #gun_hole
    gun_hole_c = kandinsky.color(0, 0, 0)
    gun_hole_h = gun_barrel_h * (20 / 100)
    gun_hole_y = gun_barrel_y
    gun_hole_w = gun_barrel_w
    gun_hole_x = gun_barrel_x
    kandinsky.fill_rect(round(gun_hole_x), round(gun_hole_y), round(gun_hole_w), round(gun_hole_h), gun_hole_c)
    if fired: #{
        gun_hole_c = kandinsky.color(255, 60, 0)
        kandinsky.fill_rect(round(gun_hole_x), round(gun_hole_y), round(gun_hole_w), round(gun_hole_h), gun_hole_c)
    #}
#}

def draw_hurt(): #{
    kandinsky.fill_rect(0, 0, SCREEN_WIDTH, round(SCREEN_HEIGHT * (10/100)), kandinsky.color(255, 0, 0))
    kandinsky.fill_rect(0, 0, round(SCREEN_WIDTH * (10/100)), SCREEN_HEIGHT, kandinsky.color(255, 0, 0))
    kandinsky.fill_rect(0, SCREEN_HEIGHT - round(SCREEN_HEIGHT * (10/100)), SCREEN_WIDTH, round(SCREEN_HEIGHT * (10/100)), kandinsky.color(255, 0, 0))
    kandinsky.fill_rect(SCREEN_WIDTH - round(SCREEN_WIDTH * (10/100)), 0, round(SCREEN_WIDTH * (10/100)), SCREEN_HEIGHT, kandinsky.color(255, 0, 0))
#}

def draw_monster(distance, x): #{
    
    monster_h = min(SCREEN_HEIGHT - 60, SCREEN_HEIGHT / (distance + 1))
    monster_w = 30

    #body
    body_c = kandinsky.color(min(255, 58 // (distance + 1) + SHADE_CORRECTION), min(255, 59 // (distance + 1) + SHADE_CORRECTION), min(255, 49 // (distance + 1) + SHADE_CORRECTION))
    body_w = monster_w
    body_h = monster_h * (80/100)
    body_x = x
    body_y = SCREEN_HEIGHT / 2 - body_h / 2 
    kandinsky.fill_rect(round(body_x), round(body_y), round(body_w), round(body_h), body_c)
    #head
    head_c = kandinsky.color(min(255, 103 // (distance + 1) + SHADE_CORRECTION), min(255, 105 // (distance + 1) + SHADE_CORRECTION), min(255, 86 // (distance + 1) + SHADE_CORRECTION))
    head_w = body_w * (60/100)
    head_h = body_h * (90/100)
    head_x = body_x + (body_w - head_w) / 2
    head_y = body_y - head_h * (60/100)
    kandinsky.fill_rect(round(head_x), round(head_y), round(head_w), round(head_h), head_c)
    #mouth
    mouth_back_c = kandinsky.color(min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION))
    mouth_back_w = head_w * (40/100)
    mouth_back_h = head_h * (90/100)
    mouth_back_x = head_x + (head_w - mouth_back_w) / 2
    mouth_back_y = head_y - mouth_back_h * (-50/100)
    kandinsky.fill_rect(round(mouth_back_x), round(mouth_back_y), round(mouth_back_w), round(mouth_back_h), mouth_back_c)
    mouth_white_c = kandinsky.color(min(255, 255 // (distance + 1) + SHADE_CORRECTION), min(255, 255 // (distance + 1) + SHADE_CORRECTION), min(255, 255 // (distance + 1) + SHADE_CORRECTION))
    mouth_white_w = mouth_back_w * (90/100)
    mouth_white_h = mouth_back_h * (5/100)
    mouth_white_x = mouth_back_x + (mouth_back_w - mouth_white_w) / 2
    mouth_white_y = mouth_back_y + mouth_back_h * (5/100)
    kandinsky.fill_rect(round(mouth_white_x), round(mouth_white_y), round(mouth_white_w), round(mouth_white_h), mouth_white_c)
    mouth_white_y = mouth_back_y + mouth_back_h - mouth_back_h * (5/100)
    kandinsky.fill_rect(round(mouth_white_x), round(mouth_white_y), round(mouth_white_w), round(mouth_white_h), mouth_white_c)
    #eyes
    eye_left_black_c = kandinsky.color(min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION))
    eye_left_black_w = head_w * (25/100)
    eye_left_black_h = head_h * (20/100)
    eye_left_black_x = head_x + eye_left_black_w / 2 
    eye_left_black_y = head_y + head_h * (20/100)
    kandinsky.fill_rect(round(eye_left_black_x), round(eye_left_black_y), round(eye_left_black_w), round(eye_left_black_h), eye_left_black_c)

    eye_left_red_c = kandinsky.color(min(255, 172 // (distance + 1) + SHADE_CORRECTION), min(255, 50 // (distance + 1) + SHADE_CORRECTION), min(255, 50 // (distance + 1) + SHADE_CORRECTION))
    eye_left_red_w = eye_left_black_w * (50/100)
    eye_left_red_h = eye_left_black_h * (30/100)
    eye_left_red_x = eye_left_black_x + eye_left_red_w / 2 
    eye_left_red_y = eye_left_black_y + eye_left_black_h * (30/100)
    kandinsky.fill_rect(round(eye_left_red_x), round(eye_left_red_y), round(eye_left_red_w), round(eye_left_red_h), eye_left_red_c)

    eye_right_black_c = kandinsky.color(min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION), min(255, 0 // (distance + 1) + SHADE_CORRECTION))
    eye_right_black_w = head_w * (25/100)
    eye_right_black_h = head_h * (20/100)
    eye_right_black_x = head_x + head_w - head_w * (40/100)
    eye_right_black_y = head_y + head_h * (20/100)
    kandinsky.fill_rect(round(eye_right_black_x), round(eye_right_black_y), round(eye_right_black_w), round(eye_right_black_h), eye_right_black_c)

    eye_right_red_c = kandinsky.color(min(255, 172 // (distance + 1) + SHADE_CORRECTION), min(255, 50 // (distance + 1) + SHADE_CORRECTION), min(255, 50 // (distance + 1) + SHADE_CORRECTION))
    eye_right_red_w = eye_right_black_w * (50/100)
    eye_right_red_h = eye_right_black_h * (30/100)
    eye_right_red_x = eye_right_black_x + eye_right_red_w / 2 
    eye_right_red_y = eye_right_black_y + eye_right_black_h * (30/100)
    kandinsky.fill_rect(round(eye_right_red_x), round(eye_right_red_y), round(eye_right_red_w), round(eye_right_red_h), eye_right_red_c)
#}

# === Helper Functions ===

def clear_screen(color): #{
    kandinsky.fill_rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, color)
#}

def render_text(text): #{
    kandinsky.draw_string(text.text, text.x, text.y, text.foreground, text.background)
#}

def render_rectangle(rectangle): #{
    kandinsky.fill_rect(rectangle.x, rectangle.y, rectangle.w, rectangle.h, rectangle.color)
#}


print("Game Started")
main()
print("Game Quit")
