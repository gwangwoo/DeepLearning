# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:47:01 2019

@author: byebye
"""

import tensorflow as tf
x_data = [1.0,2.0,3.0]
x = tf.placeholder(tf.float32)
W = tf.Variable([3.0],tf.float32)
y = W*x
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
result = sess.run(y, feed_dict={x : x_data})
print(result)