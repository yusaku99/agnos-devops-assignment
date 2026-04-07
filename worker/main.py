import time
import datetime

def do_work():
    print("Worker service starting...")
    while True:
        # Get current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Worker heartbeat at: {current_time}")
        
        # Simulated workload logic for updating timestamps
        # In a real scenario, this would persist to a database or file
        
        time.sleep(10) # Interval between tasks

if __name__ == "__main__":
    do_work()