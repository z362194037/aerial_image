# aerial_image
I am trying to draw the rectangel in the aerial image. The data of the cars and the image and description were given.

read the data and image
src_txt_dir  = "/home/gnss/learn/weixingtupian/2012-04-26-Muenchen-Tunnel_4K0G0110_pkw.samp"
img = cv2.imread('2012-04-26-Muenchen-Tunnel_4K0G0110.JPG')
plt.imshow(img)

draw the rectangel
rect = patches.Rectangle((int(arr[2])-0.5*int(arr[4]),int(arr[3])-0.5*int(arr[5])), int(arr[4]),int(arr[5]),
						fill=False,
						edgecolor='g', linewidth=1)
		t = matplotlib.transforms.Affine2D().rotate_around(float(arr[2]), float(arr[3]),\  #.rotate_around expects it's anglular argument to be in radiants
                -float(arr[6])*np.pi/180)
		rect.set_transform(t + plt.gca().transData)
    plt.gca().add_patch(rect)
