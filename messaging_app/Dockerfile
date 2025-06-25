FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /messaging_app

# 🛠️ Install OS-level dependencies including pkg-config for mysqlclient build
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev build-essential pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY Requirements.txt /messaging_app/
RUN pip install --upgrade pip && pip install -r Requirements.txt

# Copy project files
COPY . /messaging_app/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]