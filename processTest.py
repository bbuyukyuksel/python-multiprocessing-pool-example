'''
@Burak Büyükyüksel 27.02.2019 - 17:41
$ python3 processTest.py MAX
'''
import multiprocessing
import time
import threading
import json
from datetime import datetime
import sys
def logger(path, sleep_time):
    print("Logger is running..")
    global done

    while(done):
        with open(path,'a+') as f:
            f.write(str(len(multiprocessing.active_children()) ) + '\n' )
            time.sleep(0.1)

def writeFile(content):
    time.sleep(2)
    #Locked
    lock.acquire()
    with open(path, 'a+') as f:
        f.write(str(content) + '\n')
        print('(!) Section is completed.')
    lock.release()

    #Release


def init(l, p):
    global lock
    global path
    lock = l
    path = p


if __name__ == '__main__':
    done = True
    filename = 'OBJ.tmp'
    full_path = 'sources/' + filename
    OBJECTS = {filename : []}
    
    print("Başladı.")
    with open(full_path, 'r') as f:
        for line in f:
            x = eval(line)
            OBJECTS[filename].append(x)
    
    print("Content Size: ", len(OBJECTS[filename]))
    print("İçerikler okundu!")
    time.sleep(2)
    
    myLogger = threading.Thread(target=logger, args=('curr_proc_childs.log', 0.01)).start()
     
    l = multiprocessing.Lock()
    p = 'text.txt'

    start_time = datetime.now()

    SELECT_PROCESSES = {"MAX": 16, "OPT": 8, "MIN": 4, "ONE":1}
    if len(sys.argv) > 1:
        option = sys.argv[1]
    else:
        option = 'OPT'
    print("option[{}] : processes[{}]".format(option, SELECT_PROCESSES[option]))
    pool = multiprocessing.Pool(processes=SELECT_PROCESSES[option],
            initializer=init, initargs=(l,p,))
    
    pool.map(writeFile, OBJECTS[filename])
    finish_time = datetime.now()
    print(str(finish_time - start_time))
    
    pool.close()
    pool.join()
    done = False
    print("Done!")
