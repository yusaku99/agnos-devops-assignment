import time
import json
import logging
from datetime import datetime

# Custom JSON formatter for structured logging
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "service": "worker-service"
        }
        return json.dumps(log_record)

# Initialize logging
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def do_work():
    """
    Simulates a background worker process that performs tasks at intervals.
    """
    logger.info("Worker service initialized and starting background tasks...")
    
    try:
        while True:
            # Generate a heartbeat timestamp
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Log the worker's status
            logger.info(f"Worker heartbeat detected at: {current_time}")
            
            # Simulated workload: In a production environment, this could be 
            # pulling tasks from a message queue like RabbitMQ or Redis.
            
            # Wait for 10 seconds before the next iteration
            time.sleep(10)
            
    except KeyboardInterrupt:
        logger.info("Worker service is shutting down gracefully...")

if __name__ == "__main__":
    do_work()