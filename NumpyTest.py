import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

tensor1D = np.array([1.3,23,4,0.4,44])
print (tensor1D)
print (tensor1D.ndim)
print (tensor1D.shape)
print (tensor1D.dtype)
print ("===========")
#Convert python obj to tensor obj
tf_tensor = tf.convert_to_tensor(tensor1D,dtype=tf.float64)
with tf.Session() as sess:
    print (sess.run(tf_tensor))
    print (sess.run(tf_tensor[0]))