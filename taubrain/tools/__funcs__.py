import numpy as np
from nibabel.streamlines import ArraySequence
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def _get_points(array):
    x=[]
    y=[]
    z=[]
    for i in array:
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    return np.array(x), np.array(y), np.array(z)


def _get_max_point_and_min_point(streamlines):
    max_x=0
    max_y=0
    max_z=0
    min_x=0
    min_y=0
    min_z=0
    for stream in streamlines:
        for point in stream:
            if(point[0]>max_x):
                max_x=point[0]
            elif(point[1]>max_y):
                max_y=point[1]
            elif(point[2]>max_z):
                max_z=point[2]
            elif(point[0]<min_x):
                min_x=point[0]
            elif(point[1]<min_y):
                min_y=point[1]
            elif(point[0]<min_z):
                min_z=point[2]
    return ([max_x,max_y,max_z],[min_x,min_y,min_z])


def _sum_array_in_matrix(array, sum_array):
    new_array=np.zeros_like(array)
    for i in range(array.shape[0]):
        new_array[i,:]=array[i,:]+sum_array
    return new_array

def _normalize_streamlines(streamlines,sum_array):
    new_streamlines=ArraySequence()
    for stream in streamlines:
        new_streamlines.append(_sum_array_in_matrix(stream,sum_array).astype(int))
    return new_streamlines

def normalize_streamlines(streamlines)->ArraySequence:
    sum_array=_get_max_point_and_min_point(streamlines)[0]
    return _normalize_streamlines(streamlines,_get_max_point_and_min_point(streamlines)[1])

def plot_streamlines(streamlines,color='black'):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    for stream in streamlines:
        x,y,z=_get_points(stream)
        ax.plot(x,y,z)
        plt.show()

#            __
#           / _)
#    .-^^^-/ /
# __/       /
# <__.|_|-|_| -> octajos
