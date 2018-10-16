#!/usr/bin/env python
#-*- encoding: utf-8 -*-

# import Tensorflow library
import tensorflow as tf

# create constant Operation
hw = tf.constant("Hello World ! I love Tensorflow My Name is GongBiao I'm is good Enginner!")

# start a Tensorflow session
session = tf.Session()

# runing Graph
print session.run(hw)

# close Session
session.close()
