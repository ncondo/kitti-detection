#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Nicholas Condo <nicholas.condo@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Setup train, valid, and sample directories. 
"""

import os
import numpy as np
from glob import glob
from shutil import move
from shutil import copyfile


def make_dirs():
    os.mkdir('valid/')
    os.mkdir('valid/image_2/')
    os.mkdir('valid/label_2/')

    os.mkdir('sample/')
    os.mkdir('sample/train/')
    os.mkdir('sample/valid/')
    os.mkdir('sample/train/image_2/')
    os.mkdir('sample/train/label_2/')
    os.mkdir('sample/valid/image_2/')
    os.mkdir('sample/valid/label_2/')


def move_files():
    g = glob('training/image_2/*.png')
    shuf = np.random.permutation(g)
    for i in range(int(len(shuf)*.15)):
        parts = shuf[i].split('/')[-1]
        fname = parts.split('.')[0]
        move('training/image_2/'+fname+'.png', 
                'valid/image_2/'+fname+'.png')
        move('training/label_2/'+fname+'.txt', 
                'valid/label_2/'+fname+'.txt')
 
    g = glob('training/image_2/*.png')
    shuf = np.random.permutation(g)
    for i in range(400):
        parts = shuf[i].split('/')[-1]
        fname = parts.split('.')[0]
        copyfile('training/image_2/'+fname+'.png', 
                'sample/train/image_2/'+fname+'.png')
        copyfile('train/label_2/'+fname+'.txt', 
                'sample/train/label_2/'+fname+'.txt')

    g = glob('valid/image_2/*.png')
    shuf = np.random.permutation(g)
    for i in range(200):
        parts = shuf[i].split('/')[-1]
        fname = parts.split('.')[0]
        copyfile('valid/image_2/'+fname+'.png', 
                'sample/valid/image_2/'+fname+'.png')
        copyfile('valid/label_2/'+fname+'.txt', 
                'sample/valid/label_2/'+fname+'.txt')


if __name__ == '__main__':
    make_dirs()
    move_files()

