FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Disable TF (important for your setup)
ENV TRANSFORMERS_NO_TF=1

WORKDIR /app

# Install system deps (optional but useful)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]