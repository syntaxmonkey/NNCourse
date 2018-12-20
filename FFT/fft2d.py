import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import gray
from scipy import ndimage, misc
import cv2
filename = 'brickwall.jpg'
#filename = 'Leaf.png'
#leafImage = misc.imread('Leaf.png', flatten=True)
#leafImage = misc.imread(filename, flatten=True)
leafImage = cv2.imread(filename, 0)
print ( np.shape(leafImage) )

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


samplex=128 # Should have 2 linear repetitions of the structure.
sampley=128 # Should have 2 linear repetitions of the structure.
startx=550
starty=250

imageSlice = leafImage[startx:startx+samplex, starty:starty+sampley]
print( np.shape(imageSlice))
imageSlice = imageSlice / 255;
print(np.amax(imageSlice), np.amin(imageSlice))


'''
How to plot FFT:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn

plt.imshow(np.log(np.abs(np.fft.fftshift(FS))**2))
'''

plt.title(filename + '  X: ' +  str( startx ) + "  Y: " + str(starty) )
startx+=samplex
starty+=sampley

imageSlice2 = leafImage[startx:startx+samplex, starty:starty+sampley]
print( np.shape(imageSlice2))


results = np.fft.fft2(imageSlice)
#results=imageSlice

print(results)
results= np.abs(results)
results[0,0]=0
results = np.fft.fftshift(results)
#results = np.dot(results, results)
'''
print("A:",results)
results = np.log(results) # Normalize the results.
print(np.shape(results))
print("B:",results)
'''
print(np.amax(results), np.amin(results))


# FFT options
# 1. Greyscale
# 2. One channel at a time
#

# Value at origin will be the DC component.  Can be set to zero.
# Find diagonal slice that is useful.  Interim use horizontal slice as plot.
# The frequency components give a hint of the scales in the image -> based on energy distribution....

# Can we figure out the orientation of the image based on the power spectrum.  Look it up.
#
# Re-assess the gram matrix.  For dissimilar images, the dot product will produce small values while similar images will produce large values.
# Cross - reference with noise images.

'''
print(imageSlice2)

results2 = np.fft.fft2(imageSlice2)
print('FFT values:')
print(results2)

results2=np.abs(results2)  # Need to take abs first to remove imaginary components.
results2=np.dot(results2,results2)


print(results2)
'''

#results=np.abs(results-results2)

#results = results / np.max(results)


#t = np.arange(256)
#sp = np.fft.fft(np.sin(t))
#freq = np.fft.fftfreq(t.shape[-1])
#plt.plot(freq, sp.real, freq, sp.imag)
#plt.plot(freq, sp.imag)

if __name__ == '__main__':
    #plt.imshow(results, cmap='gray')
    plt.imshow(imageSlice, cmap='gray')
    plt.imshow(results)
    plt.imshow(np.log(np.abs(results) ))
    #plt.title('X: ' +  str( startx ) + "  Y: " + str(starty) )


    plt.show()
