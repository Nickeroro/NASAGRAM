import cv2
import numpy as np


def edge_detection(target):
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(target, 100, 200)
    return edges

def fourier_transform(target):
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(target)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    return magnitude_spectrum

def high_pass_filter(target):
    target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(target)
    fshift = np.fft.fftshift(f)
    rows, cols = target.shape
    crow, ccol = rows / 2, cols / 2
    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    return  img_back