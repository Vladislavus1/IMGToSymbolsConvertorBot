import cv2
from PIL import Image

PHOTOS_DIR = r"photos/"

def process_img(photo_name):
    photo = cv2.imread(PHOTOS_DIR + photo_name)
    gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    (thresh, thresh_photo) = cv2.threshold(gray_photo, 128, 255, cv2.THRESH_BINARY)
    cv2.imwrite(PHOTOS_DIR + photo_name, gray_photo)

def convert(photo_name):
    img = Image.open(PHOTOS_DIR+photo_name).convert('L')
    WIDTH, HEIGHT = img.size

    data = list(img.getdata())
    data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]
    return data





