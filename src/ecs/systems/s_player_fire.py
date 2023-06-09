from src.create.prefab_creator import create_bullet_square
from src.ecs.components.tags.c_tag_bullet import CTagBullet
import esper
import pygame
import math




def system_player_fire(world:esper.World, 
                        pos_x:int, 
                        pos_y:int, 
                        bullet_info:dict, 
                        player_info:dict,
                        max_bullets:int):

    components = world.get_components( CTagBullet )
    
    if not len(components) >= max_bullets:
        mouse_pos = pygame.mouse.get_pos()
        bullet_pos_x = pos_x+player_info["size"]["x"]/2
        bullet_pos_y = pos_y+player_info["size"]["y"]/2

        if mouse_pos[0]==bullet_pos_x:
            angle=math.radians(90)
        elif mouse_pos[1]==bullet_pos_y:
            angle=math.radians(180)
        else:
            angle = math.atan((mouse_pos[1]-bullet_pos_y)/(mouse_pos[0]-bullet_pos_x))
        
        if mouse_pos[1]<bullet_pos_y and mouse_pos[0]<bullet_pos_x:
            vel_y=-bullet_info["velocity"]*math.sin(angle)
            vel_x=-bullet_info["velocity"]*math.cos(angle)
        elif mouse_pos[1]>bullet_pos_y and mouse_pos[0]<bullet_pos_x:
            vel_y=-bullet_info["velocity"]*math.sin(angle)
            vel_x=-bullet_info["velocity"]*math.cos(angle)
        else:
            vel_y=bullet_info["velocity"]*math.sin(angle)
            vel_x=bullet_info["velocity"]*math.cos(angle)        

        return create_bullet_square(world,bullet_info, bullet_pos_x, bullet_pos_y,vel_x,vel_y)



                            