FROM python:3.12.2-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-dev \
    libtiff-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
    
COPY . /app/

RUN pip install -e .

CMD ["/bin/bash"]