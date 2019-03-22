# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:31:18 2019

@author: byebye
"""

import tensorflow as tf

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
add_val = x + y
multi_val = x * y

sess = tf.Session()

print(sess.run(add_val,feed_dict={x:10,y:20}))
print(sess.run(multi_val,feed_dict={x:10,y:20}))