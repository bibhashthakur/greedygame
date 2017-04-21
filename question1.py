import skimage.transform as st
from skimage.io import imread,imsave
import numpy as np

letters = {0:'A',1:'B',2:'C',3:'D'}

#Image Input
path = raw_input('Enter image path (Without quotes): ')
img = imread(path)
rows = img.shape[0] 
cols = img.shape[1]
print "Image Size: ",rows,cols

#Destination Coordinates
dst = []
for i in xrange(4):
	print "Enter coordinates for",letters[i],"(separated by space)"
	coord = map(int,raw_input().split())
	dst.append(coord)
	
dst = np.array(dst)
out_rows= np.max(dst[:,0])+1
out_cols= np.max(dst[:,1])+1

#Source Coordinates
src = np.array([[0,0],[cols-1,0],[cols-1,rows-1],[0,rows-1]])

#Projective Transform/ Homography
tform = st.estimate_transform('projective',src,dst)
#print tform.params
#print np.allclose(tform.inverse(tform(src)), src)

#Apply transform matrix on input image
img2 = st.warp(img,tform.inverse, output_shape=(out_rows,out_cols))
imsave('output.jpg',img2)
print '**************Image saved as output.jpg***************'
