from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import time
import yaml
import os
import sys  # Added import for sys

class Watcher:
    DIRECTORY_TO_WATCH = "./data"

    def __init__(self):
        self.observer = PollingObserver()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer stopped")
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def process(event):
        if event.src_path == './data/config.yaml':
            print(" ...changes detected, re-printing Display...\n")
            time.sleep(3)
            fancy_delay(5)
            display_interface()

    def on_modified(self, event):
        self.process(event)

def fancy_delay(duration, message=" Loading..."):
    step = duration / 100
    sys.stdout.write(f"{message} [")
    for _ in range(64):
        time.sleep(step)
        sys.stdout.write("=")
        sys.stdout.flush()
    sys.stdout.write("] Complete.\n")
    time.sleep(1)
        
def read_yaml(file_path='./data/config.yaml'):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print("Error: config.yaml not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading config.yaml: {e}")
        return None

def display_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    data = read_yaml()
    
    if data is None:
        return

    human_name = data.get('human_name')
    model_name = data.get('model_name')
    model_current = data.get('model_current')
    model_emotion = data.get('model_emotion')
    session_history = data.get('session_history')
    human_current = data.get('human_current')

    print("=" * 90)
    print("                                   Dialogue Display")
    print("=" * 90)
    print("=-" * 45)
    print(f" {human_name}'s Input:")
    print("-" * 90)
    print(f"\n {human_current}\n")
    print("=-" * 45)
    print("=-" * 45)
    print(f" {model_name}'s Response:")
    print("-" * 90)
    print(f"\n {model_current}\n")
    print("=-" * 45)
    print("=-" * 45)    
    print(f" {model_name}'s State:")
    print("-" * 90)
    print(f"\n {model_emotion}\n")  
    print("=-" * 45)
    print("=-" * 45)    
    print(" Event History:")
    print("-" * 90)
    print(f"\n {session_history}\n")
    print("=-" * 45)    
    print("=-" * 45)
    print(" Keys Status:")    
    print("-" * 90)    
    print("\n Listening for changes in './data/config.yaml'...")

if __name__ == '__main__':
    display_interface()
    w = Watcher()
    w.run()
   