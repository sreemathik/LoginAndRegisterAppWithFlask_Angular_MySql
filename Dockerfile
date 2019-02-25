FROM python:3.6

EXPOSE 5000

WORKDIR /project

COPY . /project
RUN pip install -r requirements.txt

CMD ["python", "./manage.py", "runserver"]