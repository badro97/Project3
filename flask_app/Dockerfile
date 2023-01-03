FROM python:3.9.15

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python ./app.py
# FROM python:3.9.15

# COPY . /app

# WORKDIR /app 

# RUN pip install -r requirement.txt

# CMD ["uwsgi", "uwsgi.ini"]
