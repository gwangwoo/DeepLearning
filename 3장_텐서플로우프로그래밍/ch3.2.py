#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:42:08 2019

@author: gguu
"""

import tensorflow as tf
a = tf.constant(2.5)
b = tf.constant(6.5)
sess = tf.Session()
print(sess.run(a+b))

node_a = tf.constant(2.5, tf.float32)
node_b = tf.constant(6.5)
node_c = tf.add(node_a,node_b)
print(sess.run(node_c))