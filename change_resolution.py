import os
from datetime import datetime
import shutil
from PIL import Image
import argparse
from progressbar import ProgressBar

SLASH = '/'

if os.name != 'posix':
    SLASH = '\\'


def main(args):
    PATH = args.image_folder    
    PATH_RESIZED = PATH + '{}resized'.format(SLASH)
    MAXWIDTH = args.new_width
    EXTENSIONS = ['.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.png', '.gif']

    if os.path.isdir(PATH_RESIZED):
        shutil.rmtree(PATH_RESIZED)
    
    shutil.copytree(PATH, PATH_RESIZED)

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(PATH_RESIZED):
        for file in f:            
            files.append(os.path.join(r, file))

    pb = ProgressBar(len(files))
    for f in files:
        pb.next()
        try:
            ex = f[f.index('.'):].lower()
            if ex not in EXTENSIONS:
                os.remove(f)
                continue
                        
            img = Image.open(f)
            width = img.size[0]
            if width <= MAXWIDTH:
                continue
            height = img.size[1]
            ratio = (MAXWIDTH/float(width))
            hsize = int((float(height)*float(ratio)))
            img = img.resize((MAXWIDTH,hsize))            
            img.save(f)
        except Exception as ex:
            print('Error trying to resize image {}.'.format(f))        
            print(repr(ex))
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decrease resolution of all photos in folder, if width is greater than new width. It creates a folder "resized" with the new photos.')
    parser.add_argument('image_folder', metavar='path', type=str, help='The image folder path')
    parser.add_argument('new_width', metavar='width', type=int, help='The new max width')
    args = parser.parse_args()
    main(args)
