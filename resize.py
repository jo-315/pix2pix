import os
import cv2

def resize_rectangle_img(from_dir, to_dir, size=None):

    files = [filename for filename in os.listdir(from_dir) if not filename.startswith('.')]

    for file in files:
        print(file)

        img = cv2.imread(from_dir+file, 1)

        height = img.shape[0]
        width = img.shape[1]
        x1 = y1 = 0
        x2 = width
        y2 = height
        diff = abs(height - width)

        if height > width:
            y1 = int(diff/2)
            y2 = height - y1
        elif width>height:
            x1 = int(diff/2)
            x2 = width - x1

        img = img[y1:y2,x1:x2]

        if size!=None:
            img = cv2.resize(img,(size,size))

        cv2.imwrite(to_dir+file, img)

def main():
  resize_rectangle_img('./images/original/', './images/resized/', 256)

if __name__ == '__main__':
    main()