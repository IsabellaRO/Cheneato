import numpy as np
import cv2


im = cv2.imread("passaros.jpg",cv2.IMREAD_COLOR) #Le a imagem
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Converte pro cinza
ret,thresh = cv2.threshold(imgray,127,255,0) #cinza para preto e branco
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #encontra contornos com aproximacao
contorno = (255-thresh) #inverte preto e branco

for cnt in contours: #loop 
	cnt = cnt.reshape(cnt.shape[0], 2)
# 	print('num pontos', cnt.shape[0]) #printa numero de pontos de cada array
 	media_cnt = np.sum(cnt, axis=0)/cnt.shape[0] #media dos valores dos pontos
# 	print(media_cnt)
 	cv2.circle(contorno, tuple(media_cnt), 10, (128, 128, 0))	
 	cv2.drawContours(contorno, [cnt], -1, (0, 0, 255), 3)
 	cv2.imwrite("aloka.png", contorno)
 	cv2.namedWindow("janela")
	cv2.imshow("janela", contorno)

# coord = []
# for i in contours:
# 	for j in contours:
# 		coord.append(contours[i])
# 		print(coord)




#img = cv2.drawContours(thresh, contours, -1, (0,255,0), 3)
#print(img)


# def auto_canny(image, sigma = 0.33):
#     # compute the median of the single channel pixel intensities
#     v = np.median(image)

#     # apply automatic Canny edge detection using the computed median
#     lower = int(max(0, (1.0 - sigma) * v))
#     upper = int(min(255, (1.0 + sigma) * v))
#     edged = cv2.Canny(image, lower, upper)

#     # return the edged image
#     return edged


# # Convert the frame to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # A gaussian blur to get rid of the noise in the image
# blur = cv2.GaussianBlur(gray,(5,5),25) #aumentamos o blur
# # Detect the edges present in the image
# bordas = auto_canny(blur)

# # Show the image with the contours
# cv2.imshow("contours",bordas)


# # Getting 2 arrays of the positions os x and y for the painted pixels
# vetor = np.nonzero(bordas)
# print(vetor)

# # Unifiyng the 2 2D arrays to 1 3D arrays (coordinates for Neato)
# coordinates = np.transpose(vetor)
# print(coordinates)
