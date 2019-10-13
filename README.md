# kafka-docker

Existem 2 imagens para o docker: kafka-pyclient e kafka-server
 - kafka-server: imagem centos que contém o kafka
 - kafka-pyclient: imagem que contém o programa python executando um webcrawler, que le o https://www.climatempo.com.br/ e grava no kafka-server a cada 10 segundos

--------------------- PASSO A PASSO ---------------------------------------------------------------------------------------
1) Use o terminal até chegar nos arquivos docker na "pasta docker" (yaml ou yml)

2) Execute o comenado: "docker-compose up" ou docker "stack deploy -c docker-swarm.yaml douglas-kafka"
   Irá subir um maquina com cliente onde executa o python e outra com kafka-server

3) No kafka-server, será necessário criar o topico test com o comando: 
   -- lista topicos existentes
	bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   -- Caso o topico não exista, crie com o comando abaixo
   	bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

4) verifique se o topico foi criado com o comando anterir: 
   bin/kafka-topics.sh --list --bootstrap-server localhost:9092

5) Abra o shell do producer para verificar o que está sendo gravado com o comando:
   bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

Opcional: Escreva no topico test atraves do comando:
	  bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
