#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:20:38 2019

@author: gguu
"""

import tensorflow as tf

a = tf.constant(2,tf.int32)
b = tf.constant(4,tf.int32)
c = tf.constant(6,tf.int32)
d = a*b+c
sess = tf.Session()
print(sess.run(d))