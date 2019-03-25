# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:08:35 2019

@author: byebye
"""

# [실습 7-1] 텐서플로우 프로그램으로 1씩 증가시켜 5까지 출력하는 것을 작성해보자.

import tensorflow as tf
value = tf.Variable(0, name = "increment") # 변수형 0으로 초기화 이름은 
one = tf.constant(1)    # 상수값 1 생성
new_value = tf.add(value,one) # Tensor("Add_22:0", shape=(), dtype=int32)
update = tf.assign(value, new_value) # Tensor("Assign_3:0", shape=(), dtype=int32_ref)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(value))
    for _ in range(5):
        sess.run(update)
        print(sess.run(value))