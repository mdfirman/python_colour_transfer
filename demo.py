from scipy.misc import imread, imsave
import numpy as np
import mkl

# Loading images
I0 = imread('scotland_house.png').astype(np.float64) / 255;
I1 = imread('scotland_plain.png').astype(np.float64) / 255;

# Performing colour transfer
IR_mkl = mkl.colour_transfer_MKL(I0,I1);

# Saving to disk
IR_mkl = np.clip(IR_mkl, 0, 1.0)
imsave('result_MKL.png',(IR_mkl*255).astype(np.uint8))
