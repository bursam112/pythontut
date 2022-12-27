from PIL import Image, ImageDraw
import math

def new_img_gradient(size, name):
    img = Image.new(mode='RGBA', size=size, color=(0, 0, 0, 0))

    def gradient_by_point(image):
        image1 = ImageDraw.Draw(image)
        for pixel_row in range(0, image.size[1]):  # circle formula: x^2 + y^2 = radius^2
            image1.line(xy=(-math.sqrt(-(pixel_row-image.size[0]//2)**2+(image.size[0]//2)**2)+image.size[0]//2,  # left-most x value for the circle at point y
                            pixel_row,  # y value
                            math.sqrt(-(pixel_row-image.size[0]//2)**2+(image.size[0]//2)**2)+image.size[0]//2,  # right-most x value for the circle at point y
                            pixel_row),  # y value
                        fill=(0, 0, 0, round((pixel_row/image.size[0])*255)))
        image.save(f'{name}.png')
        return image

    return gradient_by_point(img)


if __name__ == '__main__':
    new_img_gradient((1024, 1024), 'sample').show()
