FROM python:3

MAINTAINER Douglas Costa <douglas.cdias@gmail.com>


RUN mkdir /pyscript

ADD /pyscript/* /pyscript/

RUN pip3 install -r ./pyscript/requirements.txt

RUN chmod 777 /pyscript/*

#EXPOSE 5000
#HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

CMD ["python","./pyscript/KafkaProducer.py"]
