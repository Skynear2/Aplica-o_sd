# encoding=utf8
from TwitterSearch import *

try:
    #Credenciais de desenvolvedor
    ts = TwitterSearch(
        consumer_key = 'IMJh4kjQLGDzUaT9t1v0RXm5Y',
        consumer_secret = 'cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE',
        access_token = '968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf',
        access_token_secret = 'hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'
     )

        #consumer_key = 'IMJh4kjQLGDzUaT9t1v0RXm5Y',
        #consumer_secret = 'cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE',
        #access_token = '968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf',
        #access_token_secret = 'hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'

    tso = TwitterSearchOrder() #Cria variavel utilizando a api.
    tso.set_keywords(['Brasil']) #Define a palavra chave para realizar a busca de tweets.
    tso.set_language('pt') #Define idioma dos tweets.
    arquivo = open('tweets.txt', 'w') #Abre o arquivo para escrita
    

    for tweet in ts.search_tweets_iterable(tso): #Itera a lista de tweets

        msg = tweet['text'] #Armazena o tweet em uma variavem
        msg = msg.strip()
        arquivo.write(msg) #Escreve a variavel no arquivo.

    
    arquivo.close() #Fecha o arquivo

except TwitterSearchException as e:
    print(e)