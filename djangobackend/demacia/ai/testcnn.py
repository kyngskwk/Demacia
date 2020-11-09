from keras.models import load_model
from matplotlib import pyplot as plt
import cv2
model = load_model('mnist_mlp_model.h5')

model.summary()
# for i in range(8):
#     test_num = plt.imread('./images/org_trim%d.jpg' % i)
#     # test_num = (test_num > 125) * test_num
#     test_num = test_num.astype('float32') / 255.

#     plt.imshow(test_num, cmap='Greys', interpolation='nearest')
#     test_num = test_num.reshape((1, 28, 28, 1))

#     print('The Answer is ', model.predict_classes(test_num))
