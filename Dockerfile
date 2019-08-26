FROM python:3.7

ADD source/ /source
WORKDIR /source

RUN apt update
RUN pip install pipenv
RUN pipenv install

CMD ["pipenv", "run", "python3", "Simulator.py"]