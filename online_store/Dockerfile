FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/sb_rest

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/sb_rest

EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# RUN apt-get update \
#     && apt-get install netcat -y
# RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y


# COPY ./entrypoint.sh .

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]