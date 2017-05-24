#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from geometry_msgs.msg import Transform, Pose, PoseStamped, Point, Point32, PointStamped, Vector3, Vector3Stamped, Quaternion
from std_msgs.msg import Header
import tf.transformations
from move_base_msgs.msg import MoveBaseActionResult
import copy
import numpy as np
import cv2
import rospy
import geometry_msgs.msg

terminou = False

# Load the image in color
#def criaContorno(imagem): #retorna array de contornos com aprox.

	# im = cv2.imread( imagem ,cv2.IMREAD_COLOR) #Le a imagem
	# imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Converte pro cinza
	# ret,thresh = cv2.threshold(imgray,127,255,0) #cinza para preto e branco
	# cv2.imwrite('foto.png', thresh) #salva foto
	# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #encontra contornos com aproximacao
	# contorno = (255-thresh) #inverte preto e branco
	# ##cv2.imwrite('lalala.png', contorno) #salva imagem
	# for cnt in contours: #loop 
 #         cnt = cnt.reshape(cnt.shape[0], 2)
 #         media_cnt = np.sum(cnt, axis=0)/cnt.shape[0] #media dos valores dos pontos
 #         cv2.circle(contorno, tuple(media_cnt), 10, (128, 128, 0))	
 #         cv2.drawContours(contorno, [cnt], -1, (0, 0, 255), 3)
 #         cv2.imwrite("aloka.png", contorno) #cria a imagem com contorno
	# return contours


def ver_atualizacao(dado):
    if dado.status == 0 or dado.status == 1 or dado.status == 3:
        terminou = True

if __name__=="__main__":

     rospy.init_node("projetofinal")
     posicao_atual = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=1)
     #contours = criaContorno("/home/borg/catkin_ws/src/robotica16/Cheneato/scripts/linha.png")
     first_status = rospy.Subscriber("move_base/result", MoveBaseActionResult, ver_atualizacao)

     try:

        while not rospy.is_shutdown():
            pose = geometry_msgs.msg.PoseStamped()
            pose.header.frame_id = "/odom"
            lista = [(3.0,0.0),(3.0,3.0),(3.0,0.0),(0.0,0.0)]
            i=0

    #         while i < len(lista):	
    #         	if terminou == True:
				# # OS QUATRO PRIMEIROS ELEMENTOS ESTAO MUITO ESTRANHO, MAS MESMO QUANDO RETIRADOS E O NUMERÓ É DIVIDIDO POR 100, O ROBO NAO ANDA
        					
    #                      #pose.pose.position.x = round((c[i][0][0]/250.0),3)
    #                      #pose.pose.position.y = round((c[i][0][1]/250.0),3)
    #                      pose.pose.position.x = lista[i][0]
    #                      pose.pose.position.y = lista[i][1]
    #                      pose.pose.position.z = 0.0
    #                      pose.pose.orientation.x = 0.0
    #                      pose.pose.orientation.y = 0.0
    #                      pose.pose.orientation.z = 1
    #                      pose.pose.orientation.w = 1
                 
    #                      posicao_atual.publish(pose)
    #                      print(pose.pose.position.x,pose.pose.position.y)
    #                      terminou = False
    #                      i+=1
    #                      while(terminou == False):
    #                         rospy.sleep(0.1)
    #                      rospy.sleep(0.5)
    #             else:
    #             	print("fazendo nada")
    #             rospy.sleep(0.1)

                         #pose.pose.position.x = round((c[i][0][0]/250.0),3)
                         #pose.pose.position.y = round((c[i][0][1]/250.0),3)
            pose.pose.position.x = lista[0][0]
            pose.pose.position.y = lista[0][1]
            pose.pose.position.z = 0.0
            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = 1
            pose.pose.orientation.w = 1

            posicao_atual.publish(pose)
            if terminou == True:
                print("TRUE1")
                rospy.sleep(1)
            else:
                print("FALSE1")
                pose.pose.position.x = lista[0][0]
                pose.pose.position.y = lista[0][1]
                pose.pose.position.z = 0.0
                pose.pose.orientation.x = 0.0
                pose.pose.orientation.y = 0.0
                pose.pose.orientation.z = 1
                pose.pose.orientation.w = 1
                rospy.sleep(0.5)
                        
            # pose.pose.position.x = lista[1][0]
            # pose.pose.position.y = lista[1][1]
            # pose.pose.position.z = 0.0
            # pose.pose.orientation.x = 0.0
            # pose.pose.orientation.y = 0.0
            # pose.pose.orientation.z = 1
            # pose.pose.orientation.w = 1

            # posicao_atual.publish(pose)
            # if terminou == True:
            #     print("TRUE2")
            #     rospy.sleep(1)
            # else:
            #     print("FALSE2")
            #     pose.pose.position.x = lista[1][0]
            #     pose.pose.position.y = lista[1][1]
            #     pose.pose.position.z = 0.0
            #     pose.pose.orientation.x = 0.0
            #     pose.pose.orientation.y = 0.0
            #     pose.pose.orientation.z = 1
            #     pose.pose.orientation.w = 1
            #     rospy.sleep(0.5)

            # pose.pose.position.x = lista[2][0]
            # pose.pose.position.y = lista[2][1]
            # pose.pose.position.z = 0.0
            # pose.pose.orientation.x = 0.0
            # pose.pose.orientation.y = 0.0
            # pose.pose.orientation.z = 1
            # pose.pose.orientation.w = 1

            # posicao_atual.publish(pose)
            # if terminou == True:
            #     print("TRUE3")
            #     rospy.sleep(1)
            # else:
            #     print("FALSE3")
            #     pose.pose.position.x = lista[2][0]
            #     pose.pose.position.y = lista[2][1]
            #     pose.pose.position.z = 0.0
            #     pose.pose.orientation.x = 0.0
            #     pose.pose.orientation.y = 0.0
            #     pose.pose.orientation.z = 1
            #     pose.pose.orientation.w = 1
            #     rospy.sleep(0.5)
            
            # pose.pose.position.x = lista[3][0]
            # pose.pose.position.y = lista[3][1]
            # pose.pose.position.z = 0.0
            # pose.pose.orientation.x = 0.0
            # pose.pose.orientation.y = 0.0
            # pose.pose.orientation.z = 1
            # pose.pose.orientation.w = 1

            # posicao_atual.publish(pose)
            # if terminou == True:
            #     print("TRUE4")
            #     rospy.sleep(1)
            # else:
            #     print("FALSE4")
            #     pose.pose.position.x = lista[3][0]
            #     pose.pose.position.y = lista[3][1]
            #     pose.pose.position.z = 0.0
            #     pose.pose.orientation.x = 0.0
            #     pose.pose.orientation.y = 0.0
            #     pose.pose.orientation.z = 1
            #     pose.pose.orientation.w = 1
            #     rospy.sleep(0.5)

                        
                        





     except rospy.ROSInterruptException:
         print("Ocorreu uma excecao com o rospy")
