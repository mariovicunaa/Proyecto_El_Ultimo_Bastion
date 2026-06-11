from pathlib import Path

estructura = {
    "El_Ultimo_Batallon_V_Claude": {
        "main.py": "",
        "requirements.txt": "",
        "README.md": "",

        "src": {
            "__init__.py": "",

            "core": {
                "__init__.py": "",
                "game.py": "",
                "state_machine.py": "",
                "event_bus.py": "",
                "settings.py": "",
                "asset_loader.py": "",
            },

            "entities": {
                "__init__.py": "",
                "base_entity.py": "",
                "bastion.py": "",

                "enemies": {
                    "__init__.py": "",
                    "base_enemy.py": "",
                    "goblin_raider.py": "",
                    "goblin_archer.py": "",
                    "goblin_brute.py": "",
                },

                "defenses": {
                    "__init__.py": "",
                    "base_defense.py": "",
                    "archer_tower.py": "",
                    "defensive_wall.py": "",
                    "ballista.py": "",
                },
            },

            "systems": {
                "__init__.py": "",
                "wave_system.py": "",
                "combat_system.py": "",
                "resource_system.py": "",
                "build_system.py": "",
                "pathfinding.py": "",
                "map_system.py": "",
            },

            "screens": {
                "__init__.py": "",
                "main_menu.py": "",
                "gameplay.py": "",
                "pause_screen.py": "",
                "defeat_screen.py": "",
            },

            "ui": {
                "__init__.py": "",
                "hud.py": "",
                "build_panel.py": "",
                "tooltip.py": "",
                "button.py": "",
            },

            "utils": {
                "__init__.py": "",
                "timer.py": "",
                "animation.py": "",
                "math_utils.py": "",
            },
        },

        "assets": {
            "sprites": {
                "enemies": {},
                "towers": {},
                "ui": {},
                "map": {},
                "effects": {},
            },
            "sounds": {
                "sfx": {},
                "music": {},
            },
            "fonts": {},
        },

        "data": {
            "enemies.json": "{}",
            "towers.json": "{}",
            "waves.json": "{}",

            "maps": {
                "map_01.json": "{}",
            },
        },

        "tests": {
            "__init__.py": "",
            "test_wave_system.py": "",
            "test_combat_system.py": "",
            "test_resource_system.py": "",
            "test_pathfinding.py": "",
        },

        "docs": {
            "architecture.md": "",
            "game_design.md": "",
            "api_reference.md": "",
        },
    }
}


def crear_estructura(base, contenido):
    for nombre, valor in contenido.items():
        ruta = base / nombre

        if isinstance(valor, dict):
            ruta.mkdir(parents=True, exist_ok=True)
            crear_estructura(ruta, valor)
        else:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            ruta.write_text(valor, encoding="utf-8")


crear_estructura(Path("."), estructura)

print("Proyecto creado correctamente.")

