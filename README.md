# kafka-docker

Existem 2 imagens para o docker: kafka-pyclient e kafka-server
 - kafka-server: imagem centos que contém o kafka
 - kafka-pyclient: imagem que contém o programa python executando um webcrawler, que le o https://www.climatempo.com.br/ e grava no kafka-server (topico test) a cada 10 segundo

--------------------- PASSO A PASSO ---------------------------------------------------------------------------------------
1) Use o terminal até chegar na "docker", onde estão os aruqivos yaml e yml.

2) Execute o comenado: "docker-compose up" para o docker-compose.yml ou docker "stack deploy -c docker-swarm.yaml douglas-kafka" para o docker-swarm.yaml
   Irá subir um maquina com client onde executa o python e outra com kafka-server

3) No kafka-server, será necessário criar o topico test com o comando: 
   -- Verifique se o tópico já existe:
	bin/kafka-topics.sh --list --bootstrap-server localhost:9092
   -- Caso o topico não exista, crie com o comando abaixo:
   	bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

4) Após criar o topico, verifique se o topico foi criado com sucesso: 
   bin/kafka-topics.sh --list --bootstrap-server localhost:9092

5) Abra o shell do producer para verificar o que está sendo gravado com o comando:
   bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

Opcional: Escreva no topico test atraves do comando:
	  bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
