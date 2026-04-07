# Stage 1: Build stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Install dependencies into a local folder to keep the final image clean
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final execution stage
FROM python:3.9-slim
WORKDIR /app
# Copy only the installed libraries from the builder
COPY --from=builder /root/.local /root/.local
COPY main.py .

# Update PATH to use the installed packages
ENV PATH=/root/.local/bin:$PATH

# API runs on port 8080
EXPOSE 8080

CMD ["python", "main.py"]