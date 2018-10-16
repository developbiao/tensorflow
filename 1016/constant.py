# -*- coding: UTF-8 -*-

# import tensorflow libaray
import tensorflow as tf

# create constant
const1 = tf.constant([[2, 2]])
const2 = tf.constant([[4], [4]])

multiple = tf.matmul(const1, const2)

# create session object 创建session对象
sess = tf.Session()

# 用session的run方法实际运行multiple这个矩阵乘法操作
result = sess.run(multiple)

# 用print打印矩阵乘法的结果
print(result)
