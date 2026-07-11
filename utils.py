import random
import pyray as pr

colors = [
    pr.LIGHTGRAY,
    pr.GRAY,
    pr.DARKGRAY,
    pr.YELLOW,
    pr.GOLD,
    pr.ORANGE,
    pr.PINK,
    pr.RED,
    pr.MAROON,
    pr.GREEN,
    pr.LIME,
    pr.DARKGREEN,
    pr.SKYBLUE,
    pr.BLUE,
    pr.DARKBLUE,
    pr.PURPLE,
    pr.VIOLET,
    pr.DARKPURPLE,
    pr.BEIGE,
    pr.BROWN,
    pr.DARKBROWN,
    pr.WHITE,
    pr.BLACK,
]

wes_anderson = [
    pr.Color(155, 227, 249, 255),
    pr.Color(0, 151, 195, 255),
    pr.Color(242, 79, 38, 255),
    pr.Color(255, 239, 85, 255),
    pr.Color(225, 197, 163, 255),
    pr.Color(114, 223, 255, 255),
    pr.Color(250, 128, 114, 255),
    pr.Color(254, 156, 31, 255),
    pr.Color(0, 128, 128, 255),
    pr.Color(13, 13, 13, 255),
    pr.Color(230, 168, 181, 255),
    pr.Color(167, 197, 235, 255),
    pr.Color(91, 26, 24, 255),
    pr.Color(59, 154, 178, 255),
    pr.Color(235, 204, 42, 255),
    pr.Color(242, 26, 0, 255),
    pr.Color(243, 223, 108, 255),
    pr.Color(139, 175, 159, 255),
    pr.Color(221, 141, 41, 255),
    pr.Color(236, 203, 174, 255),
]


def random_hex_color() -> str:
    # Generate a random integer between 0 and 16,777,215 (0xFFFFFF)
    # Format it as a 6-digit hex string with leading zeros
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def hex_to_rgb(hex_str) -> list[int]:
    hex_str = hex_str.lstrip("#")
    return [int(hex_str[i : i + 2], 16) for i in (0, 2, 4)]


def rgb_to_hex(r, g, b) -> str:
    return f"#{r:02x}{g:02x}{b:02x}"


def hex_int_to_rgb(hex_num):
    r = (hex_num >> 16) & 0xFF
    g = (hex_num >> 8) & 0xFF
    b = hex_num & 0xFF
    return (r, g, b)


def gen_new_color():
    return random.choice([pr.RED, pr.BLUE, pr.GRAY, pr.GREEN, pr.PURPLE, pr.YELLOW])
