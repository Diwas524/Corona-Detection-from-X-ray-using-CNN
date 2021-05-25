
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import tensorflow as tf 
model = tf.keras.models.load_model('mymodel.h5')
model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])


    
def predictwin(my_dic):
    
	c='app/'+my_dic
	img = image.load_img(c, target_size=(150, 150))
	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	images = np.vstack([x])
	classes = model.predict_classes(images, batch_size=10)
	
	return classes
