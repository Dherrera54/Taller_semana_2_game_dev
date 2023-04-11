from src.ecs.components.tags.c_tag_player import CTagPlayer

import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface

def system_player_limits(world:esper.World, screen:pygame.Surface):
    screen_rect = screen.get_rect()
    components = world.get_components(CTransform, CVelocity, CSurface, CTagPlayer)

    c_t:CTransform
    c_v:CVelocity
    c_s:CSurface
    for _, (c_t, c_v, c_s, c_p) in components:
        cuad_rect = c_s.surf.get_rect(topleft=c_t.pos)

        if cuad_rect.left < 0 or cuad_rect.right > screen_rect.width:
            cuad_rect.clamp_ip(screen_rect)
            c_t.pos.x = cuad_rect.left         
            
        if cuad_rect.top < 0 or cuad_rect.bottom > screen_rect.height:
            cuad_rect.clamp_ip(screen_rect)
            c_t.pos.y = cuad_rect.top 
            
            