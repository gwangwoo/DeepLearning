#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:34:02 2019

@author: gguu
"""

# 3장 텐서플로우 프로그래밍

import tensorflow as tf
hello = tf.constant("Hello World!!")
sess = tf.Session()
print(str(sess.run(hello),encoding="utf-8"))