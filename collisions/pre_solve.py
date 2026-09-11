from pymunk import Vec2d

def pre_solve(arbiter, space, data):
    set_ = arbiter.contact_point_set
    if len(set_.points) > 0:
        user_shape = arbiter.shapes[0]
        width = (user_shape.b - user_shape.a).x
        delta = (user_shape.body.position - set_.points[0].point_a).x
        normal = Vec2d(0, 1).rotated(delta / width / 2)
        set_.normal = normal
        set_.points[0].distance = 0
    arbiter.contact_point_set = set_
    return True
