FROM python

WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN pip install -r requirements.txt

ADD . /app
WORKDIR /app

