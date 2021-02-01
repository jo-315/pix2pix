import os

import numpy
from PIL import Image
import six

import numpy as np

from io import BytesIO
import os
import pickle
import json
import numpy as np

import skimage.io as io

from chainer.dataset import dataset_mixin

class FacadeDataset(dataset_mixin.DatasetMixin):
    def __init__(
        self,
        dataDir='../images/train/',
        data_range=(1,300)
    ):

        print("load dataset start")
        print("    from: %s"%dataDir)
        print("    range: [%d, %d)"%(data_range[0], data_range[1]))

        labelDir = dataDir + 'label/'
        dataDir = dataDir + 'base/'
        self.dataDir = dataDir
        self.dataset = []

        # import file
        files = [filename for filename in os.listdir(dataDir) if not filename.startswith('.')]

        for file in files:
            img = Image.open(dataDir+file)
            label = Image.open(labelDir+file)
            label=label.convert(mode="RGB")

            w,h = img.size
            r = 256 / float(min(w,h))

            # resize images so that min(w, h) == 256
            img = img.resize((int(r*w), int(r*h)), Image.BILINEAR)
            label = label.resize((int(r*w), int(r*h)), Image.NEAREST)

            img = np.asarray(img).astype("f").transpose(2,0,1)/128.0-1.0
            label = np.asarray(label).astype("f").transpose(2,0,1)/128.0-1.0
#             label_ = np.asarray(label)-1  # [0, 12)

#             label = np.zeros((3, img.shape[1], img.shape[2])).astype("i")
#             for j in range(3):
#                 label[j,:] = label_==j

            self.dataset.append((img,label))

        print("load dataset done")

    def __len__(self):
        return len(self.dataset)

    # return (label, img)
    def get_example(self, i, crop_width=256):
        # _,h,w = self.dataset[i][0].shape
        # x_l = np.random.randint(0,w-crop_width)
        # x_r = x_l+crop_width
        # y_l = np.random.randint(0,h-crop_width)
        # y_r = y_l+crop_width
        # return self.dataset[i][1][:,y_l:y_r,x_l:x_r], self.dataset[i][0][:,y_l:y_r,x_l:x_r]
        return self.dataset[i][1], self.dataset[i][0]