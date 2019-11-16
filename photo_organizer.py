import os
from datetime import datetime
import shutil
from PIL import Image


PATH = 'C:\\Users\\rafap\\Pictures'
PATH_ORG = PATH + '\\organizadas'

try:
    if os.path.isdir(PATH_ORG):
        shutil.rmtree(PATH_ORG)
    
    os.mkdir(PATH_ORG)
    
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(PATH):
        for file in f:            
            files.append(os.path.join(r, file))
    
    for f in files:
        #date_time = Image.open(f)._getexif()[36867]
        date_time = datetime.fromtimestamp(os.path.getctime(f))
        year = date_time.year
        month = date_time.month
        
        if not os.path.isdir('{}\\{}'.format(PATH_ORG, year)):
            os.mkdir('{}\\{}'.format(PATH_ORG, year))
        if not os.path.isdir('{}\\{}\\{}'.format(PATH_ORG, year, month)):
            os.mkdir('{}\\{}\\{}'.format(PATH_ORG, year, month))
                    
        shutil.copy(f, '{}\\{}\\{}'.format(PATH_ORG, year, month))
            
except OSError:
    print ("Creation of the directory failed")

#Image.open('C:\\Users\\rafap\\Pictures\\aner_profissao.jpg')._getexif()[36867]