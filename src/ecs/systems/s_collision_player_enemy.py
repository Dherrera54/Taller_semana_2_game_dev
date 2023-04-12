from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy

import esper

def system_collision_player_enemy(world: esper.World, player_entity:int, level_cfg:dict):
    components = world.get_components(CSurface, CTransform, CTagEnemy )
    player_t = world.component_for_entity(player_entity, CTransform)
    player_s = world.component_for_entity(player_entity, CSurface)

    player_rect = player_s.surf.get_rect(topleft =  player_t.pos)

    for enemy_entity, (c_s, c_t, _) in components:
        enemy_rect = c_s.surf.get_rect(topleft = c_t.pos)
        if enemy_rect.colliderect(player_rect):
            world.delete_entity(enemy_entity)
            player_t.pos.x =  level_cfg["player_spawn"]["position"]["x"] - player_s.surf.get_width()/2
            player_t.pos.y =  level_cfg["player_spawn"]["position"]["y"] - player_s.surf.get_height()/2