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


def ver_atualizacao(goal_id): #retorna se o robo concluiu o movimento ou não (chegou no goal) e printa "chegou".
    goal_id = goal_id.status.status
    #goal foi atingido ou esta no caminho
    if goal_id == 0 or goal_id == 1 or goal_id == 3:
        terminou = True
        print("chegou")


if __name__=="__main__":

     rospy.init_node("projetofinal")
     posicao_atual = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=1)
     #contours = criaContorno("/home/borg/catkin_ws/src/robotica16/Cheneato/scripts/linha.png")
     first_status = rospy.Subscriber("move_base/result", MoveBaseActionResult, ver_atualizacao)


     try:

        while not rospy.is_shutdown():
            pose = PoseStamped()
            pose.header.frame_id = "/odom"
            lista = [(2.0,0.0),(2.0,2.0),(2.0,0.0),(0.0,0.0)]

            j=1
            lista1 = [] #lista da posição anterior (para encontrar os angulos)
            lista2= [] #lista da posição atual
            qu = [quaternion_from_euler(0,0,math.pi/2)] #
            while j < (len(lista)):
                lista1.append([round((lista[j-1][0])), round((lista[j-1][1]))])
                lista2.append([round((lista[j][0])), round((lista[j][1]))])
                delta_x = (lista2[j-1][0]-lista1[j-1][0])
                delta_y = (lista2[j-1][1]-lista1[j-1][1])
                if delta_x == 0:
                    delta_x = 0.001
                z = math.atan(delta_y/delta_x)
                quat = quaternion_from_euler(0.0, 0.0, z)
                qu.append(quat)

                j+=1

        for i in range(len(lista)):
            pose.pose.position.x = lista[i][0]
            pose.pose.position.y = lista[i][1]
            pose.pose.position.z = 0.0
            pose.pose.orientation.x = qu[i][0]
            pose.pose.orientation.y = qu[i][1]
            pose.pose.orientation.z = qu[i][2]
            pose.pose.orientation.w = qu[i][3]

            posicao_atual.publish(pose)
            if terminou == True:
                print("TRUE1")
                i+=1
                rospy.sleep(1)
                
            else:
                print("FALSE1")
                pose.pose.position.x = lista[i][0]
                pose.pose.position.y = lista[i][1]
                pose.pose.position.z = 0.0
                pose.pose.orientation.x = qu[i][0]
                pose.pose.orientation.y = qu[i][1]
                pose.pose.orientation.z = qu[i][2]
                pose.pose.orientation.w = qu[i][3]
                rospy.sleep(1)


     except rospy.ROSInterruptException:
         print("Ocorreu uma excecao com o rospy")
