import cv2
import torch

if __name__ == '__main__':
    # Read the input image
    img = cv2.imread('test.jpg')

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
