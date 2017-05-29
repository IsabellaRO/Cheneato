#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from geometry_msgs.msg import Transform, Pose, PoseStamped, Point, Point32, PointStamped, Vector3, Vector3Stamped, Quaternion
from std_msgs.msg import Header
import actionlib_msgs.msg
import tf.transformations
import copy
import numpy as np
import cv2
import rospy
from move_base_msgs.msg import MoveBaseActionResult
import math
from tf.transformations import quaternion_from_euler

terminou = False

# Load the image in color
def criaContorno(imagem): #retorna array de contornos com aprox.

    im = cv2.imread(imagem, cv2.IMREAD_COLOR) #Le a imagem
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #Converte pro cinza
    ret,thresh = cv2.threshold(imgray,127,255,0) #cinza para preto e branco
    cv2.imwrite("foto.png", thresh) #salva foto
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #encontra contornos com aproximacao
    contorno = (255-thresh) #inverte preto e branco
    ##cv2.imwrite('lalala.png', contorno) #salva imagem
    for cnt in contours: #loop 
         cnt = cnt.reshape(cnt.shape[0], 2)
         # media_cnt = np.sum(cnt, axis=0)/cnt.shape[0] #media dos valores dos pontos
         # cv2.circle(contorno, tuple(media_cnt), 10, (128, 128, 0))  
         cv2.drawContours(contorno, [cnt], -1, (0, 0, 255), 3)
         cv2.imwrite("aloka.png", contorno) #cria a imagem com contorno
    return contours


def ver_atualizacao(goal_id): #retorna se o robo concluiu o movimento ou não (chegou no goal) e printa "chegou".
    goal_id = goal_id.status.status
    #goal foi atingido ou esta no caminho
    if goal_id == 0 or goal_id == 1 or goal_id == 3:
        terminou = True
        print("chegou")


if __name__=="__main__":

     rospy.init_node("projetofinal")
     posicao_atual = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size = 1) #retorna a posição atual do robo
     contours = criaContorno("/home/borg/catkin_ws/src/robotica16/Cheneato/scripts/passaro.jpg") #chama a função cria contorno
     first_status = rospy.Subscriber("move_base/result", MoveBaseActionResult, ver_atualizacao) #retorna se o robo concluiu ou não o movimento

     try:

        while not rospy.is_shutdown(): #enquanto o robo estiver ligado
            pose = PoseStamped()
            pose.header.frame_id = "/odom"
            c = contours[1]
            i=0
            j=1
            lista1 = [] #lista da posição anterior (para encontrar os angulos)
            lista2= [] #lista da posição atual
            qu = [quaternion_from_euler(0,0,math.pi/2)] #
            while j < (c.shape[0]):
                lista1.append([round((c[j-1][0][0]/250.0),3), round((c[j-1][0][1]/250.0),3)])
                lista2.append([round((c[j][0][0]/250.0),3), round((c[j][0][1]),3)/250.0])
                delta_x = (lista2[j-1][0]-lista1[j-1][0])
                delta_y = (lista2[j-1][1]-lista1[j-1][1])
                if delta_x == 0:
                    delta_x = 0.001
                z = math.atan(delta_y/delta_x)
                quat = quaternion_from_euler(0.0, 0.0, z)
                qu.append(quat)

                j+=1
            
            while i < (c.shape[0]):
                
                pose.pose.position.x = round((c[i][0][0]/250.0),3)
                pose.pose.position.y = round((c[i][0][1]/250.0),3)
                pose.pose.position.z = 0.0
                pose.pose.orientation.x = qu[i][0]
                pose.pose.orientation.y = qu[i][1]
                pose.pose.orientation.z = qu[i][2]
                pose.pose.orientation.w = qu[i][3]

                posicao_atual.publish(pose)


                if terminou == False:
                    #se ele ainda nao chegou, o goal é repetido ate que chegue
                    print(pose.pose.position.x, pose.pose.position.y)
                    pose.pose.position.x = round((c[i][0][0]/250.0),3)
                    pose.pose.position.y = round((c[i][0][1]/250.0),3)
                    pose.pose.position.z = 0.0
                    pose.pose.orientation.x = qu[i][0]
                    pose.pose.orientation.y = qu[i][1]
                    pose.pose.orientation.z = qu[i][2]
                    pose.pose.orientation.w = qu[i][3]
                    rospy.sleep(0.5)

                i+=1
                
                rospy.sleep(1)



     except rospy.ROSInterruptException:
        print("Ocorreu uma excecao com o rospy")