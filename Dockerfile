FROM python:3

ADD ./python-script.py /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./python-script.py" ]
