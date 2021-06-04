from PIL import Image
from resizeimage import resizeimage
import os

# Inputs
input_path = input('Input the path of your files: ')
output_path = input("Input your desired output path: ")
x_input = input('Input image X size: ')
y_input = input('Input image Y size: ')


def resize_image(x_num, y_num):
    os.chdir(input_path)

    print("Resizing Images...")

    # Enter folder and separate extensions
    for filename in os.listdir(input_path):
        file_split = filename.split(".")

        # Find compatible extensions and navigate into directory
        if filename.endswith('.jpg') or filename.endswith('.png'):
            os.chdir(input_path)

            # Resize the image and save in output folder
            with open(filename, 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, [x_num, y_num])
                    os.chdir(output_path)
                    cover.save(file_split[0] + '.png', image.format)


resize_image(int(x_input), int(y_input))
