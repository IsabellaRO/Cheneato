import numpy as np
import cv2


# Load the image in color


im = cv2.imread("passaro.jpg",cv2.IMREAD_COLOR)
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
cv2.imwrite('foto.png', thresh)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contorno = (255-thresh)
cv2.imwrite('lalala.png', contorno)

print(contours)

for cnt in contours:
	cnt = cnt.reshape(cnt.shape[0], 2)
	print('num pontos', cnt.shape[0])
	media_cnt = np.sum(cnt, axis=0)/cnt.shape[0]
	cv2.circle(contorno, tuple(media_cnt), 10, (128, 128, 0))	
	cv2.drawContours(contorno, [cnt], -1, (0, 0, 255), 3)

cv2.namedWindow("janela")
cv2.imshow("janela", contorno)

# coord = []
# for i in contours:
# 	for j in contours:
# 	coord.append(contours[i])

# print(coord)

for c in contours:
	print("cont shape", c.shape)
	for i in range(c.shape[0]):
		print("x", c[i][0][0], " y", c[i][0][1])


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

