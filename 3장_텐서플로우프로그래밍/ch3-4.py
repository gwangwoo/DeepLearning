# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 23:27:07 2019

@author: byebye
"""

import tensorflow as tf

holder_data = [5,6,7,8,9]
x = tf.placeholder(tf.float32)
y= x*3
sess = tf.Session()
result = sess.run(y,feed_dict={x:holder_data})
print(result)

