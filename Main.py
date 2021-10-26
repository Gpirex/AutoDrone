import cv2
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

image = cv2.imread('quadrado.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 10, 150)
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
#_, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#,cnts, = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 3
cnts,_ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)# OpenCV 4
#cv2.drawContours(image, cnts, -1, (0,255,0), 2)

for c in cnts:
	epsilon = 0.01*cv2.arcLength(c,True)
	approx = cv2.approxPolyDP(c,epsilon,True)
	#print(len(approx))
	x,y,w,h = cv2.boundingRect(approx)
	q=0

	if len(approx)==3:
		cv2.putText(image,'Triangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==4:
		aspect_ratio = float(w)/h
		print('aspect_ratio= ', aspect_ratio)
		if aspect_ratio >= 1 and aspect_ratio <= 1.5:
			# cv2.putText(image,'Quadrado', (x,y-5),1,1,(0,255,0),1)
 		    q= 'quadrado'
			 
		else:
			cv2.putText(image,'Retangulo', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==5:
		cv2.putText(image,'Pentagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)==6:
		cv2.putText(image,'Hexagono', (x,y-5),1,1,(0,255,0),1)

	if len(approx)>10:
		cv2.putText(image,'Circulo', (x,y-5),1,1,(0,255,0),1)

	cv2.drawContours(image, [approx], 0, (0,255,0),2)
	cv2.imshow('image',image)
	cv2.waitKey(0)
	while True: 
			try:
				msg = q
				print = q
			
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