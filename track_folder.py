from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for f in os.listdir(tracked):
            src = tracked + '/' + f
            dest = destination + '/' + f
            os.rename(src, dest)
            print('file detected')

tracked = '/home/chocho/Desktop/Folder1'
destination = '/home/chocho/Desktop/Folder2'
myHandler = MyHandler()
observer = Observer()
observer.schedule(myHandler, tracked, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    observer.stop()
observer.join()