from PIL import Image, ImageDraw
import math

def new_img_gradient():
    img = Image.new(mode='RGBA', size=(100, 255), color=(0, 0, 0, 0))

    def gradient_by_point(image):
        image1 = ImageDraw.Draw(image)
        for pixel_row in range(0, image.size[1]-155):  # circle formula: x^2 + y^2 = radius^2
            image1.line(xy=(-math.sqrt(-(pixel_row-50)**2+2500)+50,  # left-most x value for the circle at point y
                            pixel_row,  # y value
                            math.sqrt(-(pixel_row-50)**2+2500)+50,  # right-most x value for the circle at point y
                            pixel_row),  # y value
                        fill=(0, 0, 0, pixel_row))
        return image

    return gradient_by_point(img)


if __name__ == '__main__':
    new_img_gradient().show()
