FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
COPY pip.conf /etc/pip.conf
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]

# EXPOSE 8080
