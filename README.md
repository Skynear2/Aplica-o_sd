# Aplicao_sd

Desenvolvida utilizando a lib TwiterSearch para Python.

Collector.py  irá coletar todos os tweets encontrados com a palavra chave Brasil.

Process.py irá processar e adicionar os dados em uma fila de mensagens.

Consumer.py irá consumir os dados.

A fila de mensagens utilizada como servidor é RabbitMQ e pode ser encontrada para download e instalação em: https://www.rabbitmq.com/download.html

Para compilar: 
python3 collector.py

python3 Process.py

python3 Consumer.py

Respeitar a ordem.
