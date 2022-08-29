def hex2num(hex):
    return int(hex, 16)


def hex_part(hex, part):
    if len(hex) == 3:
        return hex[part:part + 1] + hex[part:part + 1]
    elif len(hex) == 6:
        return hex[part * 2: (part + 1) * 2]
    else:
        raise ValueError("Invalid color: " + hex)


def hex2red(hex):
    hex = hex.removeprefix("#")
    return hex2num(hex_part(hex, 0))


def hex2green(hex):
    hex = hex.removeprefix("#")
    return hex2num(hex_part(hex, 1))


def hex2blue(hex):
    hex = hex.removeprefix("#")
    return hex2num(hex_part(hex, 2))
