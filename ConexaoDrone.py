import threading 
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_endereco = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\n PROJETO  Tello \r\n')




#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 
    try:
        msg = input("Informe a ação desejada para seu Drone: ")
        
        if not msg:
            break  

        if 'sair' in msg:
            print ('...')
            sock.close()  
            break
        
        if 'quadrado' in msg:
            msg = 'command'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            print ('iniciando o vôo...')
            time.sleep(2)

        
            print = ('decolando')
            msg = 'decolar'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(5)            
            
            #fase 1
            print = ('vertice1')
            msg = 'cw 90' #gira 90 grau sentido horário
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3) 
            
            print = ('face1')
            msg = 'forward 40' #anda 40cm em frente
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3) 
            
            
            #fase 2
            print = ('vertice2')
            msg = 'cw 90'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3) 
            
            print = ('face2')
            msg = 'forward 40'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3)       
        
            #fase 3
            print = ('vertice3')
            msg = 'cw 90'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3) 
            
            print = ('face3')
            msg = 'forward 40'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3)          
        
            #fase 4
            print = ('vertice4')
            msg = 'cw 90'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3) 
            
            print = ('face4')
            msg = 'forward 40'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(3)        
        
             #Pousar 
            print = ('Pousando...')
            msg = 'land'
            msg = msg.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_endereco)
            time.sleep(5)        
            print = ('FINALIZANDO...OBRIGADO')
        
        # envia dados
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_endereco)
    
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break