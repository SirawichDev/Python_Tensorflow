import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

#set Value a =10,b=20
a = tf.constant(10,name= "a")
b = tf.constant(20,name= "b")
#set y = a*b*2
y = tf.Variable(a * b *2,name="y")
model  = tf.global_variables_initializer()
with tf.Session() as session:
    merged = tf.summary.merge_all()
    #create File tensorflow
    writer = tf.summary.FileWriter\
        ("/tmp/tensorflowlogs",session.graph)
    session.run(model)
    print(session.run(y))