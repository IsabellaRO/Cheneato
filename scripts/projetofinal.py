#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from geometry_msgs.msg import Transform, Pose, PoseStamped, Point, Point32, PointStamped, Vector3, Vector3Stamped, Quaternion
from std_msgs.msg import Header
import tf.transformations
import copy
import numpy as np
import cv2
import rospy
import geometry_msgs.msg


# Load the image in color
def criaContorno(imagem): #retorna array de contornos com aprox.

	im = cv2.imread( imagem ,cv2.IMREAD_COLOR) #Le a imagem
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
	return contours


if __name__=="__main__":

	rospy.init_node("projetofinal")
	posicao_atual = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size = 1)
	contours = criaContorno("/home/borg/catkin_ws/src/robotica16/Cheneato/scripts/linha.png")
	# try:

	# 	while not rospy.is_shutdown():
	# 		pose = geometry_msgs.msg.PoseStamped()
	# 		pose.header.frame_id = "/odom"
	# 		for c in contours:
	# 			for i in range(c.shape[0]):
	#				x = c[i][0][0]
	#				y = c[i][0][1]
	# 				pose.pose.position.x = c[i][0][0]
	# 				pose.pose.position.y = y	
	# 				pose.pose.position.z = 0.
	# 				pose.pose.orientation.x = 0.0
	# 				pose.pose.orientation.y = 0.0
	# 				pose.pose.orientation.z = 1
	# 				pose.pose.orientation.w = 0.16

	# 				posicao_atual.publish(pose)
	# 				rospy.sleep(0.8)


	# except rospy.ROSInterruptException:
	#     print("Ocorreu uma excecao com o rospy")





	try:

		while not rospy.is_shutdown():
			pose = geometry_msgs.msg.PoseStamped()
			pose.header.frame_id = "/odom"
			for c in contours:

				for i in range(c.shape[0]):
					# OS QUATRO PRIMEIROS ELEMENTOS ESTAO MUITO ESTRANHO, MAS MESMO QUANDO RETIRADOS E O NUMERÓ É DIVIDIDO POR 100, O ROBO NAO ANDA

					pose.pose.position.x = c[i][0][0]/100
					pose.pose.position.y = c[i][0][1]/100
					pose.pose.position.z = 0.0
					pose.pose.orientation.x = 0.0
					pose.pose.orientation.y = 0.0
					pose.pose.orientation.z = 1
					pose.pose.orientation.w = 1

					posicao_atual.publish(pose)
					rospy.sleep(1)


	except rospy.ROSInterruptException:
	    print("Ocorreu uma excecao com o rospy")
