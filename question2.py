import numpy as np
from skimage.io import imread, imsave

#Image input
path = raw_input('Enter image path (Without quotes): ')
img = imread(path)
print 'Image shape:',img.shape
rows = img.shape[0]
cols = img.shape[1]

#Parameters Input
scale = int(raw_input('Enter scale to zoom (Integer>0): '))
pivot = map(int,raw_input('Enter pivot point(Separated by space): ').split())
#print pivot

#Range of Region of Interest
lowx = pivot[0] - rows/(scale*2)
highx = pivot[0] + rows/(scale*2) - 1
lowy = pivot[1] - cols/(scale*2)
highy = pivot[1] + cols/(scale*2) - 1

#Make output image
output = np.zeros((rows,cols,img.shape[2]))

#Iterate over ROI and copy pixel value 'scale**2' times in output image
i = lowx
ii=0
while i<=highx:
	#print 'i='+str(i)
	j = lowy
	jj=0	
	while j<=highy:
		#print 'j='+str(j)
		if i<0 or j<0 or i>=rows or j>=cols:
			val=[255 for x in xrange(img.shape[2])]
		else:
			val = img[i,j]
			#print val
		output[ii:ii+scale,jj:jj+scale] = val
		j+=1
		jj+=scale
	i+=1
	ii+=scale

#print output[:,:,0]
imsave('zoomed.jpg',output.astype(np.uint8))
print 'Image saved as zoomed.jpg'

