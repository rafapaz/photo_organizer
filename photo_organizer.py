import os
from datetime import datetime
import shutil
from PIL import Image
import argparse
from progressbar import ProgressBar


def organize(f, path_org, extensions):
    try:     
        ex = f[f.index('.'):].lower()
        if ex not in extensions:
            return
        
        date_time = Image.open(f)._getexif()[36867]
        year = date_time.split(' ')[0].split(':')[0]
        month = date_time.split(' ')[0].split(':')[1]        
    except Exception:
        print('Error trying to get exif date: {}. Getting creation date file instead.'.format(f))        
        date_time = datetime.fromtimestamp(os.path.getctime(f))
        year = date_time.year
        month = date_time.month
    
    if not os.path.isdir('{}\\{}'.format(path_org, year)):
        os.mkdir('{}\\{}'.format(path_org, year))
    if not os.path.isdir('{}\\{}\\{}'.format(path_org, year, month)):
        os.mkdir('{}\\{}\\{}'.format(path_org, year, month))
                
    shutil.copy(f, '{}\\{}\\{}'.format(path_org, year, month))

def main(args):
    PATH = args.image_folder
    PATH_ORG = PATH + '\\organized'
    EXTENSIONS = ['.jpg', '.jpeg', '.tif', '.tiff', '.bmp', '.png', '.gif']

    if os.path.isdir(PATH_ORG):
        shutil.rmtree(PATH_ORG)

    os.mkdir(PATH_ORG)

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(PATH):
        for file in f:            
            files.append(os.path.join(r, file))

    pb = ProgressBar(len(files))
    for f in files:
        pb.next()
        organize(f, PATH_ORG, EXTENSIONS)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize your photos by year and month it was taken. It generates a folder "organized" with a copy of your photos.')
    parser.add_argument('image_folder', metavar='path', type=str, help='The image folder path')
    args = parser.parse_args()
    main(args)