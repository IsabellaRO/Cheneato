import numpy as np
import cv2

# Load the image in color
def criaContorno(imagem): #retorna array de contornos com aprox.

	im = cv2.imread(imagem ,cv2.IMREAD_COLOR) #Le a imagem
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Converte pro cinza
	ret,thresh = cv2.threshold(imgray,127,255,0) #cinza para preto e branco
	cv2.imwrite('foto.png', thresh) #salva foto
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #encontra contornos com aproximacao
	contorno = (255-thresh) #inverte preto e branco
	##cv2.imwrite('lalala.png', contorno) #salva imagem
	for cnt in contours: #loop 
		cnt = cnt.reshape(cnt.shape[0], 2)
	# 	print('num pontos', cnt.shape[0]) #printa numero de pontos de cada array
	 	media_cnt = np.sum(cnt, axis=0)/cnt.shape[0] #media dos valores dos pontos
	# 	print(media_cnt)
	 	cv2.circle(contorno, tuple(media_cnt), 10, (128, 128, 0))	
	 	cv2.drawContours(contorno, [cnt], -1, (0, 0, 255), 3)
	 	cv2.imwrite("aloka.png", contorno) #cria a imagem com contorno
	 	for c in contours:
	#		print("cont shape", c.shape)
			for i in range(c.shape[0]):
				print("x", c[i][0][0], " y", c[i][0][1])
	return c[i][0][0], c[i][0][1]

