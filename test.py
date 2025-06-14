import carla

client = carla.Client('localhost', 2000)
world = client.get_world()
client.load_world("Town01")
blueprints = world.get_blueprint_library()
spawn_points = world.get_map().get_spawn_points()

ego_bp= blueprints.find("vehicle.doodge_charger_police")
ego_bp.set_attribute("role_name", "hero")
ego_vehicle = world.spawn_actor(ego_bp, spawn_points[0])

