import tensorflow as tf
import input_data
mnist = input_data.read_data_sets("/data/", one_hot = True)
tf.set_random_seed(777)
 
learning_rate = 0.001
training_epochs = 10
batch_size = 100
 
X = tf.placeholder(tf.float32, [None, 784])
X_img = tf.reshape(X, [-1, 28, 28, 1])
Y = tf.placeholder(tf.float32, [None, 10])
 
 
W1 = tf.Variable(tf.random_normal([3, 3, 1, 32], stddev = 0.01))
L1 = tf.nn.conv2d(X_img, W1, strides = [1, 1, 1, 1], padding = 'SAME')
L1 = tf.nn.relu(L1)
L1 = tf.nn.max_pool(L1, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
 
 
W2 = tf.Variable(tf.random_normal([3, 3, 32, 64], stddev = 0.01))
L2 = tf.nn.conv2d(L1, W2, strides = [1, 1, 1, 1], padding = 'SAME')
L2 = tf.nn.relu(L2)
L2 = tf.nn.max_pool(L2, ksize = [1, 2, 2, 1], strides = [1, 2, 2, 1], padding = 'SAME')
L2_flat = tf.reshape(L2, [-1, 7*7*64])
 
W3 = tf.Variable(tf.random_normal([7*7*64, 10], stddev = 0.01))
b = tf.Variable(tf.random_normal([10]))
logits = tf.matmul(L2_flat, W3) + b
 
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = Y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)
correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
 
 
# 텐서보드 활용하기 위한 스칼라 정의
cost_train_sum = tf.summary.scalar("cost_train", cost)
accuracy_train_sum = tf.summary.scalar("accuracy_train", accuracy)
 
 
sess = tf.Session()
sess.run(tf.global_variables_initializer())
 
 
# 모델 저장을 위한 부분
import os
save_file = './model_mnist.ckpt'
SAVER_DIR = "modelMNIST"
saver = tf.train.Saver()
checkpoint_path = os.path.join(SAVER_DIR, "modelMNIST")
ckpt = tf.train.get_checkpoint_state(SAVER_DIR)
 
# 텐서보드 
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter('./mygraph/train', sess.graph)
writer_test = tf.summary.FileWriter('./mygraph/test', sess.graph)
 
 
print('Learning Started')
for epoch in range(training_epochs):
    avg_cost = 0
    avg_cost_test = 0
    total_batch = int(mnist.train.num_examples / batch_size)
    
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(bach_size)
        feed_dict = {X: batch_xs, Y: batch_ys}
        summary, c, a, _ = sess.run([merged, cost, accuracy, optimizer], feed_dict = feed_dict)
        avg_cost += c / total_batch
        
        batch_test_xs, batch_test_ys = mnist.test.next_batch(batch_size)
        feed_dict_test = {X: batch_test_xs, Y: batch_test_ys}
        summary_test, c_test, a_test = sess.run([merged, cost, accuracy], feed_dict = feed_dict_test)
        avg_cost_test += c_test / total_batch
        
    print('Epoch: ', '%04d' % (epoch+1), 'Train cost = ', '{:.9f}'.format(avg_cost))
    print('Epoch: ', '%04d' % (epoch+1), 'Train acc = ', '{:.9f}'.format(a))
    print('Epoch: ', '%04d' % (epoch+1), 'Test cost = ', '{:.9f}'.format(avg_cost_test))
    print('Epoch: ', '%04d' % (epoch+1), 'Test acc = ', '{:.9f}'.format(a_test))
    print('\n')
    
    # Tensorboard에서 epoch별 스칼라값 확인하기 위함
    writer.add_summary(summary, global_step = epoch)
    writer_test.add_summary(summary_test, global_step = epoch)
    
    # epoch별 모델 체크포인트 저장
    saver.save(sess, checkpoint_path, global_step = epoch)
 
print('Learning finished')
writer.close()
saver.save(sess, save_file)
