from classes.Brick import Brick
from data import constants

def generateLevel1(screen, space, brick_shapes):
    w, h = constants.BRICK['WIDTH'], constants.BRICK['HEIGHT']
    cols = int(480 // (w + constants.PADDING))
    center_col = (cols - 1) / 2 
    center_row = constants.ROWS / 2
    radius = min(cols, constants.ROWS) / 2.5 #die groesse
    for row in range(constants.ROWS + 1):
        for col in range(cols):
            dx = col - center_col
            dy = row - center_row
            distance_from_center = (dx ** 2 + dy ** 2) ** 0.5  # Pythagoras

            if distance_from_center <= radius:
                x = col * (w + constants.PADDING) + constants.PADDING + 75
                y = screen.get_height() - (row * (h + constants.PADDING) + constants.TOP_OFFSET)
                box = Brick(
                    space, 
                    brick_shapes,
                    (x, y)
                )

    return 1