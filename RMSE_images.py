# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:28:46 2020

@author: Bruker
"""
import numpy as np

#remember to convert images to arrays

def RMSE_img(image_x,image_y):
    error=np.sqrt(np.mean(np.square(image_x-image_y)))
    return error