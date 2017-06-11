import os, sys
import glob
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot, transforms
from scipy import ndimage
import matplotlib as mpl
import matplotlib.patches as patches
import matplotlib
import numpy as np
#from rlpy.Domains.Domain import Domain
#import matplotlib.patches as mpatches
src_txt_dir  = "/home/gnss/learn/weixingtupian/2012-04-26-Muenchen-Tunnel_4K0G0110_pkw.samp"

#plt.cla()
img = cv2.imread('2012-04-26-Muenchen-Tunnel_4K0G0110.JPG')
plt.imshow(img)

img_dir = "/home/gnss/learn/weixingtupian"
with open(src_txt_dir, "r") as f:
	for line in f.readlines():
		arr = line.split(" ")
		img_path = arr[0]
		#print img_path
		img_position_x = arr[2]
		img_position_y = arr[3]
		print img_position_x,img_position_y



		
		rect = patches.Rectangle((int(arr[2])-0.5*int(arr[4]),int(arr[3])-0.5*int(arr[5])), int(arr[4]),int(arr[5]),
						#int(arr[4]) - int(arr[2]),
						#int(arr[5]) - int(arr[3]), 
						fill=False,
						edgecolor='g', linewidth=1)
		t = matplotlib.transforms.Affine2D().rotate_around(float(arr[2]), float(arr[3]),\
                -float(arr[6])*np.pi/180)
		rect.set_transform(t + plt.gca().transData)
		#rotation = mpl.transforms.Affine2D().rotate_deg_around(
        #    int(arr[2]),int(arr[3]),int(arr[6]) + plt.gca().transData
        #rect.set_transform(rotation)
		plt.gca().add_patch(rect)
		#rot = transforms.Affine2D().rotate_deg(arr[6])
		#my_plot=plt.Rectangle((int(arr[2])-int(arr[4]),int(arr[3])-int(arr[5])), int(arr[4]),int(arr[5]),
						#int(arr[4]) - int(arr[2]),
						#int(arr[5]) - int(arr[3]), 
		#				fill=False,
		#				edgecolor='g', linewidth=1)
		#plt.gca().add_patch(
			#Rotated_Plot = ndimage.rotate(my_plot, 30)
						
						#(0,255,0),3)
#plt.axis('equal')
#plt.axis('off')
			#)
#plt.draw()
		#rot = transforms.Affine2D().rotate_deg(arr[6])
#plt.title('{}  {:.3f}'.format(class_name, score))
plt.show()

