from PIL import Image # pip install pillow
import os

downloads_fldr = "C:/Users/varmi/Downloads/"
images_fldr = "C:/Users/varmi/OneDrive/Pictures/Saved_by_Python/"

if __name__ == '__main__':
    for filename in os.listdir(downloads_fldr):
        name, extension = os.path.splitext(downloads_fldr + filename)
        if extension in ['.jpg', '.png', '.jpeg']:
            picture = Image.open(downloads_fldr + filename)
            picture.save(downloads_fldr + "compressed_"+filename, optimize=True, quality=60)
            print(name + ": " + extension)