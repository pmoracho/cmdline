from progressbar import ProgressBar
from progressbar import FormatLabel
from progressbar import Percentage
from progressbar import Bar
from progressbar import RotatingMarker
from progressbar import ETA
import time

def main():

    print("Executing main")

    f = 1
    t = 10
    widgets = [FormatLabel(''), ' ', Percentage(), ' ', Bar('#'), ' ', ETA(), ' ', RotatingMarker()]
    bar = ProgressBar(widgets=widgets, maxval=t)

    for i in range(1, t+1):
        widgets[0] = FormatLabel('[Contador: {0}]'.format(i))
        time.sleep(1)
        bar.update(i)

    bar.finish()