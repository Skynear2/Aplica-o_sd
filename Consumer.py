# encoding=utf8
import threading
import time
import pika

class Consumer:
    def __init__(self):
        
        t1 = threading.Thread(target=self.workerEsporte,args=()) #Cria thread de esportes.
        t1.start()#Inicia a thread.

        t2 = threading.Thread(target=self.workerPolitica ,args=()) #Cria thread de Politica.
        t2.start()#Inicia a thread.

        t3 = threading.Thread(target=self.workerOutros,args=()) #Cria thread de Outros.
        t3.start()#Inicia a thread.
        

    def callbackE(self,ch, method, properties, body): #Callback quer será utilizado ao consumir mensagens.
            arquivo = open('Esporte.txt', 'a') #Abre o arquivo de saida.
            arquivo.write(str(body, 'utf-8')) #Grava a mensagem recebida no arquivo de saida.
            arquivo.write('\n') #quebra linhda
            print("Topico esporte recebeu: ", str(body, 'utf-8'))  #Imprime no console a mensagem recebida realizando um cast de bytes para String
            
            

    def callbackP(self, ch, method, properties, body):
            arquivo = open('Politica.txt', 'a')  #Abre o arquivo de saida.
            arquivo.write(str(body, 'utf-8')) #Grava a mensagem recebida no arquivo de saida.
            arquivo.write('\n') #quebra linhda
            print("Topico Politica recebeu: ", str(body, 'utf-8') ) #Imprime no console a mensagem recebida realizando um cast de bytes para String
            
            
    
    def callbackO(self, ch, method, properties, body):
            if(str(body, 'utf-8') == "\n"):
                return
            else:
                arquivo = open('Outros.txt', 'a')  #Abre o arquivo de saida.
                arquivo.write(str(body, 'utf-8')) #Grava a mensagem recebida no arquivo de saida.
                arquivo.write('\n') #quebra linhda
                print("Topico outros recebeu: ",str(body, 'utf-8')) #Imprime no console a mensagem recebida realizando um cast de bytes para String
             
            


    def workerEsporte(self):
        
        self.connectionE = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #Define a conexão com o servidor de filas de mensagens.
        self.channelE = self.connectionE.channel() #Define o canal de comunicação utilizado para receber mensagens. Cada thread possui sua propria conexão e canal de comunicação
        
        print("Iniciando thread esporte.")
        
        self.channelE.basic_consume(queue='Esporte', on_message_callback=self.callbackE, auto_ack=True)#Define qual fila de mensagem será consumida.
        
        print(' [*] Esperando mensagens sobre esporte.')
        
        self.channelE.start_consuming()#Começa a consumir as mensagens recebidas no canal.
        
        print("Thread encerrada esporte.")

    def workerPolitica(self):
        
        self.connectionP = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #Define a conexão com o servidor de filas de mensagens.
        self.channelP = self.connectionP.channel() #Define o canal de comunicação utilizado para receber mensagens. Cada thread possui sua propria conexão e canal de comunicação
        
        print("Iniciando thread politica.")
        
        self.channelP.basic_consume(queue='Politica', on_message_callback=self.callbackP, auto_ack=True)#Define qual fila de mensagem será consumida.
        
        print(' [*] Esperando mensagens sobre politica.')
        
        self.channelP.start_consuming() #Começa a consumir as mensagens recebidas no canal.
        
        print("Thread encerrada politica .")

    def workerOutros(self):
        
        self.connectionO = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #Define a conexão com o servidor de filas de mensagens.
        self.channelO = self.connectionO.channel() #Define o canal de comunicação utilizado para receber mensagens. Cada thread possui sua propria conexão e canal de comunicação
        
        print("Iniciando thread outros.")
        
        self.channelO.basic_consume(queue='Outros', on_message_callback=self.callbackO, auto_ack=True)#Define qual fila de mensagem será consumida.
        
        print(' [*] Esperando mensagens sobre outros.')
        
        self.channelO.start_consuming()#Começa a consumir as mensagens recebidas no canal.
        
        print("Thread encerrada outros. ")
    
    
    def print(self, tweet):
        for obj in tweet:
            print(obj)
            print('----')

if __name__ == '__main__':            
    teste = Consumer()
