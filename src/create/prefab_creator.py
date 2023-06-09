from src.ecs.components.tags.c_tag_player import CTagPlayer
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bullet import CTagBullet
import random
import pygame
import esper
from src.ecs.components.c_enemy_spawner import CEnemySpawner

from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

from src.ecs.components.c_input_command import CInputCommand

def create_square(world:esper.World, size:pygame.Vector2,
                    pos:pygame.Vector2, vel:pygame.Vector2, col:pygame.Color) -> int:
    cuad_entity = world.create_entity()
    world.add_component(cuad_entity,
                CSurface(size, col))
    world.add_component(cuad_entity,
                CTransform(pos))
    world.add_component(cuad_entity, 
                CVelocity(vel))

    return cuad_entity

def create_enemy_square(world:esper.World, pos:pygame.Vector2, enemy_info:dict):
    size = pygame.Vector2(enemy_info["size"]["x"], 
                          enemy_info["size"]["y"])
    color = pygame.Color(enemy_info["color"]["r"],
                         enemy_info["color"]["g"],
                         enemy_info["color"]["b"])

    vel_x=random_vel_generator(enemy_info['velocity_min'], 
                               enemy_info['velocity_max']) 
    vel_y=random_vel_generator(enemy_info['velocity_min'], 
                               enemy_info['velocity_max']) 
 
    
    velocity = pygame.Vector2(vel_x,
                              vel_y)
    enemy_entity = create_square(world, size, pos, velocity, color)
    world.add_component(enemy_entity, CTagEnemy())

def random_vel_generator(min_value:int,max_value:int):
    return random.randint(min_value, max_value) * random.choice([1, -1])

def create_player_square(world:esper.World,  palyer_info:dict, player_lvl_info:dict) -> int:
    size = pygame.Vector2(palyer_info["size"]["x"], 
                          palyer_info["size"]["y"])
    color = pygame.Color(palyer_info["color"]["r"],
                         palyer_info["color"]["g"],
                         palyer_info["color"]["b"])  
    pos =  pygame.Vector2(player_lvl_info["position"]["x"]-size.x/2, 
                          player_lvl_info["position"]["y"]-size.y/2)

    vel = pygame.Vector2(0,0)   

    player_entity = create_square(world, size,pos,vel,color)
    world.add_component(player_entity, CTagPlayer())
    return player_entity

def create_bullet_square(world:esper.World,  
                            bullet_info:dict, 
                            bullet_pos_x:float, 
                            bullet_pos_y:float,
                            vel_x:float, 
                            vel_y:float) -> int:
    size = pygame.Vector2(bullet_info["size"]["x"], 
                          bullet_info["size"]["y"])
    color = pygame.Color(bullet_info["color"]["r"],
                         bullet_info["color"]["g"],
                         bullet_info["color"]["b"])  
    pos =  pygame.Vector2(bullet_pos_x, bullet_pos_y)

    vel = pygame.Vector2(vel_x,vel_y)   

    bullet_entity = create_square(world, size,pos,vel,color)
    world.add_component(bullet_entity, CTagBullet())
    return bullet_entity


def create_enemy_spawner(world:esper.World, level_data:dict):
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity,
                        CEnemySpawner(level_data["enemy_spawn_events"]))

def create_input_player(world:esper.World):
    input_left = world.create_entity()
    input_right = world.create_entity()
    input_up = world.create_entity()
    input_down = world.create_entity()
    input_mouse_click = world.create_entity()

    world.add_component(input_left,
                        CInputCommand("PLAYER_LEFT", pygame.K_LEFT))
    world.add_component(input_right,
                        CInputCommand("PLAYER_RIGHT", pygame.K_RIGHT))
    world.add_component(input_up,
                        CInputCommand("PLAYER_UP", pygame.K_UP))
    world.add_component(input_down,
                        CInputCommand("PLAYER_DOWN", pygame.K_DOWN))
    world.add_component(input_mouse_click,
                        CInputCommand("PLAYER_FIRE", pygame.BUTTON_LEFT))