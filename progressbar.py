import sys

class ProgressBar:
    
    def __init__(self, total):
        self.total = total
        self.count = 0
        self.perc = 0
        self.bar = ''
    
    def next(self):
        self.count = self.count + 1
        self.perc = (self.count * 100)/self.total
        self.bar = '='*int(self.perc/5)
        sys.stdout.write('|                    | [ {}% ]'.format(int(self.perc)))
        sys.stdout.write('\r|')
        sys.stdout.write('{}'.format(self.bar))
        sys.stdout.write('\r')
        sys.stdout.flush()