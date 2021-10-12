import csv
import numpy as np
import os
import pathlib
from PIL import Image
from sklearn.preprocessing import normalize
from sklearn.preprocessing import MinMaxScaler

def read_from_csv(dir):

    result = [] # array
    with open(dir,'r')as file:
        filecontent=csv.reader(file)
        result = list(filecontent)
    # print(result)

    return result


def read_from_csv_2(dir,val):

    dir = dir + str(val)+'.csv'

    result = [] # array
    with open(dir,'r')as file:
        filecontent=csv.reader(file)
        result = list(filecontent)
    # print(result)

    return result


def vector_plot_3d(x,y,z):
    u = np.sin(np.pi * float(x)) * np.cos(np.pi * float(y)) * np.cos(np.pi * float(z))
    v = -np.cos(np.pi * float(x)) * np.sin(np.pi * float(y)) * np.cos(np.pi * float(z))
    w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * float(x)) * np.cos(np.pi * float(y)) * np.sin(np.pi * float(z)))

    return u,v,w


def save_data(dirname,data,type):
    dirout = '../results/'+str(type)
    directory = os.path.dirname(dirout)
    pathlib.Path(dirout).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(directory):
        os.makedirs(directory)

    np.savetxt(str(dirout) + '/' +str(dirname) + '.csv', data, delimiter=',')
    

    # dirname = "concave20.obj_T" + format(trials, '03d') + "_N00"


def save_master(filename,data):
    dirout = '../results/'
    directory = os.path.dirname(dirout)
    pathlib.Path(dirout).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(directory):
        os.makedirs(directory)
    np.savetxt(str(dirout) + '/' +str(filename) + '.csv', data, delimiter=',')

def append_data_to_list(list,data):

    if float(data) < 100:
        list.append(float(data))
    else:
        print("data seems too large! Data: ", data)
        pass

def convert_to_RGB(volume: np.ndarray, index: int):
    scaler = MinMaxScaler(feature_range=(0, 255))
    rvolume = scaler.fit_transform(volume.reshape(-1, volume.shape[-1])).reshape(volume.shape)
    img_arr = Image.fromarray(rvolume[:, :, index])
    if img_arr.mode != 'RGB':
        img_arr= img_arr.convert('RGB')
    # if img_arr.mode == "F" or img_arr.mode == "I":
    #     img_arr = img_arr.convert('L')
    return rvolume, img_arr


def convert_contact_to_gray(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                data[i][j] = 255
            else:
                data[i][j] = 0
    
    img_arr = Image.fromarray(np.uit8(data),'L')


    return img_arr


def save_image(dirname,data,type):
    dirout = '../results/images/' + str(type) + '/'
    directory = os.path.dirname(dirout)
    pathlib.Path(dirout).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(directory):
        os.makedirs(directory)
    img_dir = dirout+str(dirname)+'.jpg'
    data.save(img_dir)

