# encoding=utf8

import threading
import time
import pika

class Process:
    def __init__(self, text):
        self.esporte = [] #Cria lista para tweets de esporte
        self.politica = []#Cria lista para armazenar tweets de politica.
        self.outros = []#Cria lista para armazenar tweets outros.
        self.tweets = []#Cria lista para armazenar tweets lidos.

        self.lerTweet(text) #Chama método para ler tweets do arquivo.
    
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #Define a conexão com a fila de mensagens.
        self.channel = self.connection.channel() #Define o canal de comunicação com a fila de mensagens.

        self.declaraQueue() #Cria as filas de mensagens.
        
        t = threading.Thread(target=self.worker,args=()) #Cria uma thread para o processamento dos tweets
        t.start() #Inicia Thread


    def declaraQueue(self):
        #Declarando as filas
        self.channel.queue_declare(queue='Esporte') #Declara fila de esportes
        self.channel.queue_declare(queue='Politica') #Declara fila de politica
        self.channel.queue_declare(queue='Outros') #Declara fila de variados

    def lerTweet(self, text):
        for obj in text: #itera no arquivo de tweets
                self.tweets.append(obj) #Adiciona na lista de tweets

    def worker(self):
        print("Iniciando thread.")
        for obj in self.tweets: #itera na lista de tweets
            #If = verifica a existência de palavras chaves pré-definidas com o assunto politica.
            
            if(('Bolsonaro' in obj) or ('governo' in obj) or ('Crivela' in obj) or ('PT' in obj) or ('Lula' in obj) or ('Haddad' in obj) or ('Eduardo Bolsonaro' in obj) or ('Flavio Bolsonaro' in obj) or ('Paulo Guedes' in obj)):
                
                self.politica.append(obj) #caso encontre adiciona na lista de tweets de politica.
                
                self.channel.basic_publish(exchange='',routing_key='Politica',body=obj) #Publica o tweet na fila de mensagens sobre politica.
                self.tweets.remove(obj)
                pass
            
            elif (('futebol' in obj) or ('Flamengo' in obj) or ('Palmeiras' in obj) or ('volei' in obj) or ('Neymar' in obj) or ('Campeonado Brasileiro' in obj) or ('Copa do brasil' in obj) or ('libertadores' in obj)):
                #Elif = verifica a existência de palavras chaves pré-definidas com o assunto esporte.
                
                self.esporte.append(obj) #caso encontre adiciona na lista de tweets de esporte.
        
                self.channel.basic_publish(exchange='',routing_key='Esporte',body=obj) #Publica na fila de mensagens com o assunto Esporte.
                self.tweets.remove(obj)
                pass
            else:
                #Else = Caso o tweet não encontre nenhuma palavra chave sobre esporte ou politica adiciona na lista outros.
                self.outros.append(obj) #adiciona na lista de mensagens outros.
                self.channel.basic_publish(exchange='',routing_key='Outros',body=obj) #Publica na fila de mensagens de assunto outros.
                self.tweets.remove(obj)

        #Conversão para % para informar.
        total = len(self.esporte) + len(self.politica) + len(self.outros)
        print(total, 'tweets analisados.')
        
        print(str(int((len(self.esporte) * 100)/total))+"%"+ "("+str(len(self.esporte))+") " +"tweets de esporte.")
        
        print(str(int((len(self.politica) * 100)/total))+"%"+ "("+str(len(self.politica))+") " +"tweets de politica.")
        
        print(str(int((len(self.outros) * 100)/total))+"%"+ "("+str(len(self.outros)) +") "+"tweets de outros.")
        
        print("Thread encerrada.")
    
    def print(self, tweet):
        for obj in tweet:
            print(obj)
            print('----')

if __name__ == '__main__':                       
    arquivo = open('tweets.txt', 'r')
    teste = Process(arquivo.readlines())
