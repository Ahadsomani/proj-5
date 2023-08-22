import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "<Set path for tracking file system events>"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
        else:
            print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        if event.is_directory:
            print(f"Directory moved/renamed: {event.src_path} -> {event.dest_path}")
        else:
            print(f"File moved/renamed: {event.src_path} -> {event.dest_path}")

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
        else:
            print(f"File deleted: {event.src_path}")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=from_dir, recursive=True)
observer.start()

try:
    print("Observer is running. Press any key to stop.")
    input()
except KeyboardInterrupt:
    pass

observer.stop()
observer.join()
print("Observer stopped.")
