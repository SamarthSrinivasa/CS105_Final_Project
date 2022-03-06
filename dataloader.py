
from skimage import io


## INPUT PARAMS
IMG_WIDTH = 1200
IMG_HEIGHT = 600


def load_data(filename):
    image = io.imread('img/Thinking-of-getting-a-cat.png')
    image_data = (image).reshape(1200*600, 3)
    return image_data
    # 