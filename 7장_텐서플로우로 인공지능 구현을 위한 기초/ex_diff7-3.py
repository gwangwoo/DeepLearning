# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 04:03:32 2019

@author: byebye
"""

import tensorflow as tf
before = 0
now = 1
lr = 0.001
precision = 0.5
def diff(x):
    return 0.1*2*(x+5)

for step in range(11):
    before = now
    now = before - lr*diff(before)
    
    print("미분수 ㅣ",step, "Local Minimum : ", now)

    
