import cv2
from PIL import Image

PHOTOS_DIR = r"photos/"


def process_img(photo_name):
    photo = cv2.imread(PHOTOS_DIR + photo_name)
    gray_photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(PHOTOS_DIR + photo_name, gray_photo)


def convert(photo_name):
    img = Image.open(PHOTOS_DIR+photo_name).convert('L')
    WIDTH, HEIGHT = img.size

    data = list(img.getdata())
    data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]
    with open(photo_name+".txt", "w", encoding="utf-8") as file:
        for binary_line in data:
            file.write(''.join(["█" if 0 <= pixel < 62 else "▓" if 62 < pixel < 124 else "▒" if 124 < pixel < 186 else "░" if 186 < pixel < 255 else " " if pixel==255 else " " for pixel in binary_line])+"\n")
    file.close()
    return photo_name+".txt"




