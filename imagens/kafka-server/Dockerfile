FROM centos:7
MAINTAINER Douglas Costa Dias<douglas.cdias@gmail.com>

ENV SCALA_VERSION 2.11
ENV KAFKA_VERSION 2.2.1
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"

WORKDIR /tmp

RUN yum -y install java-1.8.0-openjdk

RUN yum -y install bash zip wget

RUN wget https://www-eu.apache.org/dist/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \
    tar -xzf kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz kafka_"$SCALA_VERSION"-"$KAFKA_VERSION" && \
    mv kafka_"$SCALA_VERSION"-"$KAFKA_VERSION" $KAFKA_HOME
    
RUN rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz

ENV PATH $KAFKA_HOME:$PATH

WORKDIR $KAFKA_HOME
ADD run.sh $KAFKA_HOME/run.sh
RUN chmod a+x $KAFKA_HOME/run.sh
EXPOSE 9092
EXPOSE 2181
CMD ["run.sh"]
