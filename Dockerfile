FROM python:3.7-alpine

COPY bots/config_bot.py /bots/
COPY bots/stream.py /bots/
COPY bots/dynamo.py /bots/
COPY bots/firehose.py /bots/

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "stream.py"]