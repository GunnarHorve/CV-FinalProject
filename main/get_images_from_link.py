import urllib2
import urllib
from urllib2 import Request
import cv2
import numpy as np
import os

dir_path = './neg'


def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04461879'
    neg_images_request = Request(neg_images_link)
    neg_image_urls = urllib2.urlopen(neg_images_request).read()
    pic_num = 0

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print("Yaya")
    else:
        return

    for i in neg_image_urls.split('\n'):
        try:
            # loop maintenance
            print(i)
            pic_num += 1

            # ???
            neg_image_url = dir_path + '/' + str(pic_num) + ".jpg"

            # downloading and saving image to 100x100 python object
            urllib.urlretrieve(i, neg_image_url)
            img = cv2.imread(neg_image_url, cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))

            # saving image to local filesystem
            cv2.imwrite(neg_image_url, resized_image)

        except Exception as e:
            print(str(e))


def find_uglies():
    match = False
    for file_type in [dir_path]:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('uglies/' + str(ugly))
                    question = cv2.imread(current_image_path)
                    if question:
                        if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
                            print('That is one ugly pic! Deleting!')
                            print(current_image_path)
                            os.remove(current_image_path)
                    else:
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


store_raw_images()
find_uglies()

#https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
