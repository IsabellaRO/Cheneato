#! /usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = ["Rachel P. B. Moraes", "Fabio Miranda"]

import rospy
import numpy
from numpy import linalg
import transformations
from tf import TransformerROS
import tf2_ros
import math
from geometry_msgs.msg import Twist, Vector3, Pose, Vector3Stamped
from ar_track_alvar_msgs.msg import AlvarMarker, AlvarMarkers
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from neato_node.msg import Bump # BUMP
from sensor_msgs.msg import LaserScan#BUMP

x = 0
y = 0
z = 0 
ls = 0
rs = 0
lf = 0
rf = 0
volte = False
right = False
left = False

id = 0

tfl = 0
tf_buffer = tf2_ros.Buffer()



def recebe(msg):
	global x # O global impede a recriacao de uma variavel local, para podermos usar o x global ja'  declarado
	global y
	global z
	global id
	global tfl
	global tf_buffer
	global buffer


	#frame = "head_camera" # Quando for rodar no simulador com webcam
	frame = "camera_frame" # Quando for rodar no robo


if __name__=="__main__":
#	global tfl 
#	global buffer
	global velocidade_saida
	rospy.init_node("Cheneato") # Como nosso programa declara  seu nome para o sistema ROS

	velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3) # Para podermos controlar o robo

	tfl = tf2_ros.TransformListener(tf_buffer) # Para fazer conversao de sistemas de coordenadas - usado para calcular angulo
	

	try:
		# Loop principal - todo programa ROS deve ter um
		while not rospy.is_shutdown():
			print("Rodando loop principal")
			velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
			velocidade_saida.publish(velocidade)

			rospy.sleep(0.1)
			if id == 100:
				print ("z: ",z)
				print ("z desejado: ",z_desejado)
				if z_desejado < z-0.3:
				 	print("Vá para frente")
				 	vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				 	velocidade_saida.publish(vel)

				elif z-0.3 <= z_desejado and z_desejado <= z+0.3:
		 	 		print("Z CERTO")
		 	 		vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
		 	 		velocidade_saida.publish(vel)
					 
				else:
				 	print("Vá para trás")
				 	vel = Twist(Vector3(-0.5, 0, 0), Vector3(0, 0, 0))
			 		velocidade_saida.publish(vel)

				print("Estou na área A!")
				print ("x: ",x)
				print ("x desejado: ",x_desejado)

				if x_desejado < x-0.3:
					print("Vá para direita")
					vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.2))
					velocidade_saida.publish(vel)
					vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				  	velocidade_saida.publish(vel)
					vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0.2))
					velocidade_saida.publish(vel)

				elif x-0.3 <= x_desejado and x_desejado >= x+0.3:
					print("X CERTO")
					vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
		 		 	velocidade_saida.publish(vel)

				else:
					print("Vá para esquerda")
					vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.2))
					velocidade_saida.publish(vel)
					vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				  	velocidade_saida.publish(vel)
					vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0.2))
					velocidade_saida.publish(vel)


			else:
				print("Não encontrei o marcador 100")
				vel = Twist(Vector3(0,0,0), Vector3(0,0,0))
				velocidade_saida.publish(vel)


		elif volte == True:
			print("Vá para trás")
		 		vel = Twist(Vector3(-2, 0, 0), Vector3(0, 0, 0))
		 		velocidade_saida.publish(vel)

		 		volte = False
		 		rospy.sleep(0.4)
		 		vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
		 		velocidade.saida.publish(vel)
		 		rospy.sleep(0.1)

		 	elif left == True:
		 		print("Vá para direita")
			vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.5))
			velocidade_saida.publish(vel)
			rospy.sleep(0.4)
			vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				velocidade_saida.publish(vel)
				rospy.sleep(0.4)
			left = False
			vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
		 		velocidade.saida.publish(vel)
		 		rospy.sleep(0.1)

		elif right == True:
			print("Vá para esquerda")
			vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, -0.5))
			velocidade_saida.publish(vel)
			rospy.sleep(0.4)
			vel = Twist(Vector3(0.5, 0, 0), Vector3(0, 0, 0))
				velocidade_saida.publish(vel)
				rospy.sleep(0.4)
			right = False
			vel = Twist(Vector3(0,0,0),Vector3(0,0,0))
		 		velocidade.saida.publish(vel)
		 		rospy.sleep(0.1)


		rospy.sleep(0.1)

	except rospy.ROSInterruptException:
		print("Ocorreu uma exceção com o rospy")