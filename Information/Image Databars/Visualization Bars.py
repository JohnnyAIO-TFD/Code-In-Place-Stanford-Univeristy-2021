"""
Image Visualization Project.
"""
from simpleimage import SimpleImage

GREEN = 127
BLUE = 127

CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 200


def main():
    canvas = SimpleImage.blank(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.show()


if __name__ == '__main__':
    main()
