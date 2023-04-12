from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

import esper

def system_collision_bullet_enemy(world: esper.World):
    
    components_enemies = world.get_components(CSurface, CTransform, CTagEnemy )
    components_bullets = world.get_components(CSurface, CTransform, CTagBullet )

    for enemy_entity, (c_s_e, c_t_e, _) in components_enemies:
        enemy_rect = c_s_e.surf.get_rect(topleft = c_t_e.pos)
        for bullet_entity,(c_s_b, c_t_b, _) in components_bullets:
            bullet_rect = c_s_b.surf.get_rect(topleft = c_t_b.pos)
            if enemy_rect.colliderect(bullet_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)
            