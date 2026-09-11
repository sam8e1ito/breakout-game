from features import powerup_feature


def _remove_powerup(space, key, powerup_shape):
    if powerup_shape.body in space.bodies:
        space.remove(powerup_shape, powerup_shape.body)


def on_powerup_collected(arbiter, space, data):
    powerup_shape = arbiter.shapes[0]
    try:
        powerup = powerup_shape.powerup_type
    except AttributeError:
        return False

    space.add_post_step_callback(_remove_powerup, powerup_shape, powerup_shape)
    powerup_feature.processPowerup(powerup, space, arbiter)
    return False


def on_powerup_missed(arbiter, space, data):
    powerup_shape = arbiter.shapes[0]
    space.add_post_step_callback(_remove_powerup, powerup_shape, powerup_shape)
    return False
