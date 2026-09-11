def isSecretBrick(brick_shape):
    try:
        if brick_shape.user_data:
            return True
    except AttributeError:
        return False