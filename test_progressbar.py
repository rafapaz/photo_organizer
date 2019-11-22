
from progressbar import ProgressBar

TOTAL = 100000

pb = ProgressBar(TOTAL)

for i in range(TOTAL):
    pb.next()
