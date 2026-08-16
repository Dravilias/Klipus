FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir yt-dlp

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]