# messaging_app/Dockerfile

# Step 1: Use Python 3.10 base image
FROM python:3.10-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Set work directory
WORKDIR /app

# Step 4: Install dependencies
COPY Requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r Requirements.txt

# Step 5: Copy project files
COPY . /app/

# Step 6: Expose Django's default port
EXPOSE 8000

# Step 7: Run Django server (adjust if using manage.py elsewhere)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
