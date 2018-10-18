# -*- coding: utf-8 -*-

# import tensorflow
import tensorflow as tf

# construct Graph struct
# 用一个线性方程的例子 y = W * x + b
W = tf.Variable(2.0, dtype=tf.float32, name="Weight") # 权重
b = tf.Variable(1.0, dtype=tf.float32, name="Bias") # 偏差
x = tf.placeholder(dtype=tf.float32, name="Input") # 输入

with tf.name_scope("Output"):   # 输出的命名空间
    y = W * x + b # 输出

# 定义保存日志的路径
path = "./log"

# 创建用于初始所有变量 (Variable) 的操作
init = tf.global_variables_initializer()

# 创建Session会话
with tf.Session() as sess:
    sess.run(init) # 初始化变量
    writer = tf.summary.FileWriter(path, sess.graph)
    result = sess.run(y, {x: 3.0})
    print("y = %s result" % result) # 打印 y = W * x + b = 7;
