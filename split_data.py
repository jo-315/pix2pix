
import shutil
import random
import os

def main():
  files = [filename for filename in os.listdir('./images/resized') if not filename.startswith('.')]

  for file in files:
      print(file)
      rand_num = random.random()
      if rand_num < 0.9:
          shutil.copy('./images/resized/'+file, './images/train/base/'+file)
          shutil.copy('./images/canny/'+file, './images/train/label/'+file)
      else:
          shutil.copy('./images/resized/'+file, './images/test/base/'+file)
          shutil.copy('./images/canny/'+file, './images/test/label/'+file)

if __name__ == '__main__':
    main()