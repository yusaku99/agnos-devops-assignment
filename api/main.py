import logging
import json
from datetime import datetime

# Custom JSON formatter
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "service": "api-service"
        }
        return json.dumps(log_record)

logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Agnos API Service"}

@app.get("/health")
def health_check():
    # Kubernetes uses this to check if the app is alive
    return {"status": "healthy"}

@app.post("/process")
async def process_data(data: dict):
    # This is where your main logic would go
    logger.info(f"Processing data: {data}")
    return {"message": "Data received and processing started", "data": data}