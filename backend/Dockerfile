FROM python:3.11-slim-buster

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ssh \
    build-essential \
    libpq-dev \
    curl \
    fonts-thai-tlwg \
    && rm -rf /var/lib/apt

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python","main.py"]
