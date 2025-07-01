from pynput.mouse import Listener as MouseListener

def writetofile(x,y):
    print('Position of the current mouse {0}'.format((x,y)))

with MouseListener(on_move=writetofile) as lis:
    lis.join()