FROM python:3.10-alpine
RUN apk update
RUN apk add --no-cache py3-pip
RUN mkdir /app
COPY requirements.txt app.py /app/
WORKDIR /app/
RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python", "/app/app.py"]

