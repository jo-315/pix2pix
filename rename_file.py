
import glob
import os
import shutil

path = "./images/original"
path_af = "./images/original"
files = glob.glob(path + '/*')

start_num = 0

for i, f in enumerate(files):
    print(f)

    # 連番でファイル名をつける
    f_name = 'img_' + "{0:05d}".format(i + start_num) + '.png'

    # rename
    os.rename(f, os.path.join(path, f_name))

    # 別フォルダからcopyする場合
    # shutil.copyfile(f, os.path.join(path_af, f_name))

    print(f_name)