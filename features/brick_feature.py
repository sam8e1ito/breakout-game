def isSecretBrick(brick_shape):
    return getattr(brick_shape, 'secret', False)

def isScoreBrick(brick_shape):
    return getattr(brick_shape, 'score', False)