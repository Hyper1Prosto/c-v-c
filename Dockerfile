from python:3.11-alpha

#работа папки 
WORKDIR /app

#копируем зависимости
COPY req.txt .

RUN pip install --no--cache-dir -r req.txt

COPY . .
CMD ["python3", "main.py"]