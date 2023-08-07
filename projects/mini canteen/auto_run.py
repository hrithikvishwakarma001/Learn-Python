import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.process = None

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            if self.process:
                self.process.terminate()
                self.process.wait()
            print("Restarting script...")
            self.process = Popen(['python', self.script_path])

def main():
    if len(sys.argv) < 2:
        print("Usage: python auto_run.py your_script.py")
        return

    script_path = sys.argv[1]
    
    event_handler = RestartHandler(script_path)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
