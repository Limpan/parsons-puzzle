FROM python:3.5

MAINTAINER Linus Törngren <linus@etnolit.se>

ENV INSTALL_PATH /code

ADD . $INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN pip install -r requirements.txt
CMD ["./manage.py", "run"]
