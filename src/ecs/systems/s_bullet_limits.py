from src.ecs.components.tags.c_tag_bullet import CTagBullet

import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface

def system_bullet_limits(world:esper.World, screen:pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CSurface, CTagBullet)

    c_t:CTransform

    c_s:CSurface
    for bullet_entity, (c_t, c_s, c_p) in components:
        bullet_rect = c_s.surf.get_rect(topleft=c_t.pos)

        if bullet_rect.left < 0 or bullet_rect.right > screen_rect.width:
            world.delete_entity(bullet_entity)               
            
        if bullet_rect.top < 0 or bullet_rect.bottom > screen_rect.height:
            world.delete_entity(bullet_entity)
            
            