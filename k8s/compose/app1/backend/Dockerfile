FROM python:3.7
COPY . /app
WORKDIR /app
RUN ["pip3", "install", "-r", "requirements.txt", "-i", "http://mirrors.aliyun.com/pypi/simple/", "--trusted-host", "mirrors.aliyun.com"]
#EXPOSE 5000
CMD ["python3", "app.py"]