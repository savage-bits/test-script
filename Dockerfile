FROM python:3

ADD ./python-script.py /

RUN pip install --upgrade pip
RUN pip install --upgrade requests

ENTRYPOINT [ "python", "./python-script.py" ]
