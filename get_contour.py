import os
import numpy as np
from matplotlib import pyplot as plt

import cv2

def save_canny_img(from_path, to_path):
    img = cv2.imread(from_path)
    canny_img = cv2.Canny(img, 200, 300, apertureSize=3)
    cv2.imwrite(to_path, canny_img)

def main():
  files = [filename for filename in os.listdir('./images/resized') if not filename.startswith('.')]  
  for file in files:
    print(file)
    save_canny_img('./images/resized/'+file, './images/canny/'+file)

if __name__ == '__main__':
    main()