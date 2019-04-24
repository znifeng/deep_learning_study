import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

import tensorflow as tf

##Define input data format
#input images, each image is represented by a tensor of 784 dimensions
x = tf.placeholder("float", [None,784])
#input labels, each label values one digit of [0,9], which is represented by a tensor of 10 dimensions
y_ = tf.placeholder("float", [None, 10])

##Define Model and algorithm
#weight array of each feature VS predicted result
W = tf.Variable(tf.zeros([784, 10]))
#bias of each digit
b = tf.Variable(tf.zeros([10]))
#predicted probability array of an image, which is of 10 dimensions.
y = tf.nn.softmax(tf.matmul(x,W) + b)
#cross-entropy or called loss function
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#gredient descent algorithm
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

##Training model
#initialize all variables
tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

##Evaluation 
#tf.argmax(y,1) returns the maxi
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
