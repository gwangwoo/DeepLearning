# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:45:35 2019

@author: byebye
"""
# [실습 7-2] 연결 가중치 행렬 W와 바이어스 b 값을 경사 하강법으로 찾는 프로그램을 작성해보자
# 예측 값을 구할 식은 H = tf.matmul(W,x) + b

import tensorflow as tf
import numpy as np

x = np.float32(np.random.rand(2,100)) # 2행 100열의 텐서 생성
# 학습 레이블(목표값)은 아래식으로 정의(W = [0.2,0.4], b = 0.6)
y_data = np.dot([0.200,0.400],x) + 0.600 # 1행2열 , 2행 100열 행렬 연산
b = tf.Variable(tf.zeros([1])) # b는 0 b의 1개 요소를 0으로 초기화
# W는 1x2 형태의 연결가중치 변수
W = tf.Variable(tf.random_uniform([1,2],-1.0,1.0)) # 1행 2열 초기화
H = tf.matmul(W,x)+b # 입력 데이터 x와 W,b를 사용해 선형모델 정의
#cost(loss) 와 학습함수르 정의, 제곱 합으로 평균을 구함
cost = tf.reduce_mean(tf.square(H-y_data)) #cost 함수정의
# 경사하강법으로 cost(loss) 함수가 최소가 되는 값을 구함(0.5는 학습비율)
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(cost)
# 학습 세션 시작.
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)
print("학습수 cost값        W 두개 값              b값")
for step in range(201): # 200번 학습
    sess.run(train) # train 실행
    if step % 20 == 0:
        print(step,sess.run(cost),sess.run(W),sess.run(b))