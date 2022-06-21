FROM python:3.9

# WORKDIR /usr/src/sb_rest
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install netcat -y
RUN apt upgrade -y && apt install postgresql gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r req.txt

COPY ./entrypoint.sh .

COPY . .
# COPY . /usr/src/sb_rest

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
# EXPOSE 8000





# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# RUN apt-get update \
#     && apt-get install netcat -y
# RUN apt-get upgrade -y && apt-get install postgresql gcc python3-dev musl-dev -y


# COPY ./entrypoint.sh .

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]