FROM python:3.6-alpine
RUN apk add --no-cache gcc
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/
COPY . .
ENTRYPOINT ["gunicorn","app:app","-c","gunicorn.conf.py"]
#CMD ["python","app.py"]