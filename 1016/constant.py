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

if const1.graph is tf.get_default_graph():
	print("const1所在的图 (Graph)是当前default graph")

# close session
sess.close()

# 第二第方法来创建和关闭Session
with tf.Session() as sess:
	result2 = sess.run(multiple)
	print("Multiple的结果是:%s " % result2)
