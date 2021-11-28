

def vector2d(x:float,y:float) -> list:

    return [x,y]


def normalize(vec2d:list) -> list:

    #Vector auf Länge 1 bringen
    
    mag = magnitude(vec2d)
    vec2d[0] /= mag
    vec2d[1] /= mag

    return vec2d


def magnitude(vec2d:list) -> float:

    mag:float = vec2d[0] ** 2 + vec2d[1] ** 2
    mag **= 0.5

    return mag
