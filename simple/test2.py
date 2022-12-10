from PIL import Image
import math

BLACK, DARKGRAY, GRAY = ((0, 0, 0), (63, 63, 63), (127, 127, 127))
LIGHTGRAY, WHITE = ((191, 191, 191), (255, 255, 255))
BLUE, GREEN, RED = ((0, 0, 255), (0, 255, 0), (255, 0, 0))


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def rot_x(self, degrees):
        radians = math.radians(degrees)
        return self.x * math.cos(radians) + self.y * math.sin(radians)


class Rect(object):
    def __init__(self, x1, y1, x2, y2):
        minx, maxx = (x1, x2) if x1 < x2 else (x2, x1)
        miny, maxy = (y1, y2) if y1 < y2 else (y2, y1)
        self.min = Point(minx, miny)
        self.max = Point(maxx, maxy)

    def min_max_rot_x(self, degrees):
        first = True
        for x in [self.min.x, self.max.x]:
            for y in [self.min.y, self.max.y]:
                p = Point(x, y)
                rot_d = p.rot_x(degrees)
                if first:
                    min_d = rot_d
                    max_d = rot_d
                else:
                    min_d = min(min_d, rot_d)
                    max_d = max(max_d, rot_d)
                first = False
        return min_d, max_d

    width = property(lambda self: self.max.x - self.min.x)
    height = property(lambda self: self.max.y - self.min.y)


def gradient_color(minval, maxval, val, color_palette):
    """ Computes intermediate RGB color of a value in the range of minval
        to maxval (inclusive) based on a color_palette representing the range.
    """
    max_index = len(color_palette) - 1
    delta = maxval - minval
    if delta == 0:
        delta = 1
    v = float(val - minval) / delta * max_index
    i1, i2 = int(v), min(int(v) + 1, max_index)
    (r1, g1, b1), (r2, g2, b2) = color_palette[i1], color_palette[i2]
    f = v - i1
    return int(r1 + f * (r2 - r1)), int(g1 + f * (g2 - g1)), int(b1 + f * (b2 - b1))


def degrees_gradient(im, rect, color_func, color_palette, degrees):
    minval, maxval = 1, len(color_palette)
    delta = maxval - minval
    min_d, max_d = rect.min_max_rot_x(degrees)
    range_d = max_d - min_d
    for x in range(rect.min.x, rect.max.x + 1):
        for y in range(rect.min.y, rect.max.y + 1):
            p = Point(x, y)
            f = (p.rot_x(degrees) - min_d) / range_d
            val = minval + f * delta
            color = color_func(minval, maxval, val, color_palette)
            im.putpixel((x, y), color)


def gradient_image(color_palette, degrees):
    region = Rect(0, 0, 600, 400)
    width, height = region.max.x + 1, region.max.y + 1
    image = Image.new("RGB", (width, height), WHITE)
    degrees_gradient(image, region, gradient_color, color_palette, -degrees)
    return image


if __name__ == '__main__':
    # Draw a three color vertical gradient.
    color_palette = [BLUE, GREEN, RED]
    region = Rect(0, 0, 730, 350)
    width, height = region.max.x + 1, region.max.y + 1
    image = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(image)
    vert_gradient(draw, region, gradient_color, color_palette)
    image.show()
    # image.save("vert_gradient.png", "PNG")
    # print('image saved')
