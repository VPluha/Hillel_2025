FROM python:3.13-slim

WORKDIR /app

# Ставимо залежності
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код і тести
COPY app/main.py .
COPY tests/ ./tests

# Додаємо /app до PYTHONPATH, щоб pytest бачив main.py
ENV PYTHONPATH=/app

# Запуск pytest
CMD ["pytest", "-v", "tests/"]
