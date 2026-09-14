from classes.Brick import Brick
from data import state, constants

def generateLevel2(screen, space, brick_shapes):
    w, h = constants.BRICK['WIDTH'], constants.BRICK['HEIGHT']
    cols = int(480 // (w + constants.PADDING))
    center_col = (cols - 1)/ 2
    base_gap = 1.0
    freeColsRow1 = [1, 2, 3, cols - 2, cols - 3, cols - 4]
    freeColsRow2 = [1, 2, cols - 2, cols -3]
    for row in range(constants.ROWS + 1):
        gap_half_width = base_gap + row * 1.0
        for col in range(cols):
            distance_from_center = abs(col - center_col) 
            if row == 1:
                if col in freeColsRow1:
                    col += 1
                    continue
            elif row == 2:
                if col in freeColsRow2:
                    col += 1
                    continue
            elif row == 3:
                if col == 1 or col == cols - 2:
                    col += 1
                    continue
            if distance_from_center >= gap_half_width:
                x = col * (w + constants.ROWS) + constants.ROWS + 75
                y = screen.get_height() - (row * (h + constants.ROWS) + constants.TOP_OFFSET)
                box = Brick( 
                    space, 
                    brick_shapes,  
                    (x, y)
                    )
    return 2