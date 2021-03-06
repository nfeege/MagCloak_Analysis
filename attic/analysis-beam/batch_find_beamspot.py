from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

def beamSpot(ref_image, image_input, path, show_plots):
	#Ben Coe, Stony Brook ePHENIX Magnetic Cloaking Division
	#October 1, 2014
	#This code here reads in two data png files from the command line
	#and finds the distance between the important beam spots,
	#then converts that to the distance traversed by the beam spot
	#then converts that to the angle the beam moved
	#Then it prints it all, including the two pictures with the important spot
	#circled in red, so that we can make sure qualitatively that it found
	#them correctly


	##Import stuff
	import matplotlib.pyplot as plt
	import matplotlib.image as mpimg
	from skimage import data
	from skimage.feature import blob_dog, blob_log, blob_doh
	from skimage.color import rgb2gray
	import numpy as np
	import matplotlib.image
	import sys

	#Declare Stuff
	#pipe_distance is distance of beam pipe from magnet to screen in mm
	#screen_angle is angle of the screen in degrees
	#conversion is roughly the conversion from mm to pixels
	#Since screen angle is 45 degrees, the image we see on the screen from 90 degrees
	#is the same as the image would be on a sraight screen, so we don't really need
	#screen_angle, but it's here anyway. Ideally, only using conversion and
	#pipe_distance should give us everything we need
	conversion = .1
	pipe_distance = 1000
	screen_angle = 45

	#Read in images and switch them to grayscale from RGB
	image = mpimg.imread(path+ref_image)
	image_gray = rgb2gray(image)
	image2 = mpimg.imread(path+image_input)
	image2_gray = rgb2gray(image2)
	imagelist = [image, image2]

	#Run this to get hessian matrices and find the centers and std deviations
	#We'll need to adjust the threshold and max_sigma to be sure we accurately pick
	#up our beam spot, but it's pretty simple to tune that
	blobsy = blob_doh(image_gray, max_sigma=30, threshold=.001)
	blobsy2 = blob_doh(image2_gray, max_sigma=30, threshold=.001)
	blobsylist = [blobsy, blobsy2]

	#Find the largest standard deviation in each (should be largest/main blob that
	#we care about), we'll keep this for what we need
	main_blob = np.argmax(blobsy, axis = 0)[2]
	main_blob2 = np.argmax(blobsy2, axis = 0)[2]
	mainlist = [main_blob, main_blob2]

	#Set Titles
	titlelist =['1','2']

	#Shove it all together to loop it
	sequence = zip(blobsylist, mainlist, imagelist, titlelist)

	#Declare distance variable
	coords = []

	#Loop, for each image, draw the circle and print it all so we can check it
	for blobs, mains, images, titles in sequence:

		#Draw a circle around the important one
		fig, ax = plt.subplots(1,1)
		ax.imshow(images, interpolation = 'nearest')
		ax.set_title(titles)
		y, x, r = blobs[mains]
		coords.append([x,y])
		c = plt.Circle((x,y), r, color = 'red', linewidth = 2, fill = False)
		ax.add_patch(c)
		
	#coords now has coordinates of the centers, here we find their x distance
	pix_distance = np.absolute(coords[0][0] - coords[1][0])

	#Transform to spatial coordinates
	mm_distance = conversion * pix_distance

	#Calculate angle
	angle = 2*np.arctan((mm_distance/2)/(pipe_distance))
	degrees = angle*180 / np.pi

	#Print it all
	print_output = False
	if print_output:
		print('Pixels traversed: ',pix_distance,' pixels')
		print('Millimeters traversed: ', mm_distance, 'mm')
		print('Angle traversed: ', angle, 'rad, or ', degrees,'degrees')
	list_output = [image_input, pix_distance, mm_distance, angle]
	plt.close()
	if show_plots:
		plt.show()
	return list_output

mypath = '/home/josh/github/analysis-beam/images/Test_2014_10_30/'
#mypath = '/home/josh/github/analysis-beam/images/wip/'
onlyfiles = sorted([f for f in listdir(mypath) if (isfile(join(mypath, f)) and f.endswith(".png"))])
#print '\n'.join(onlyfiles)

full_list = []
ref_image = 'beam_2014_10_30_027.png'
for image in onlyfiles:
	if image != ref_image:
		image_list = beamSpot(ref_image, image, mypath, False)
		plt.close()
		full_list.append(image_list)

print(full_list)
x = [0.363, 0.363, 0.363, 0.363, 0.363, 0.413, 0.413, 0.413, 0.413, 0.413, 0.463, 0.463, 0.463, 0.463, 0.463, 0.313, 0.313, 0.313, 0.313, 0.313, 0.263, 0.263, 0.263, 0.263]
y = []
for image in full_list:
#	x.append(image[3])
	y.append(image[2])

plt.plot(x, y, 'ro')
plt.ylabel("Millimeters Travelled")
plt.xlabel("HE Steerer I X")
plt.show()








