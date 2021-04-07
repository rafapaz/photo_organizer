import os
from datetime import datetime
import shutil
import ffmpeg
import argparse
from progressbar import ProgressBar


def organize(f, path_org, extensions):
    try:     
        ex = f[f.index('.'):].lower()
        if ex not in extensions:
            return
        
        video = ffmpeg.probe(f)
        data = video['streams'][0]['tags']['creation_time']        
        year = int(data.split('-')[0])
        month = int(data.split('-')[1])
    except Exception as error:
        print(repr(error))
        print('Warning: canot get video date: {}. Getting creation date file instead.'.format(f))        
        date_time = datetime.fromtimestamp(os.path.getctime(f))
        year = date_time.year
        month = date_time.month
    
    if not os.path.isdir('{}\\{}'.format(path_org, year)):
        os.mkdir('{}\\{}'.format(path_org, year))
    if not os.path.isdir('{}\\{}\\{}'.format(path_org, year, month)):
        os.mkdir('{}\\{}\\{}'.format(path_org, year, month))
                
    shutil.copy(f, '{}\\{}\\{}'.format(path_org, year, month))

def main(args):
    PATH = args.video_folder
    PATH_ORG = PATH + '\\videos-organized'
    EXTENSIONS = ['.webm', '.mkv', '.flv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.gifv', '.mng', '.avi', '.MTS', '.M2TS', '.TS',
         '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.viv', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', 
         '.mpe', '.mpv', '.mpg', '.mpeg', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b']

    print(PATH_ORG)
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
    parser = argparse.ArgumentParser(description='Organize your videos by year and month it was taken. It generates a folder "videos-organized" with a copy of your videos. Attention: you need to download the ffmpeg binaries from https://ffmpeg.org/download.html and set your PATH to point to them.')
    parser.add_argument('video_folder', metavar='path', type=str, help='The video folder path')
    args = parser.parse_args()
    main(args)