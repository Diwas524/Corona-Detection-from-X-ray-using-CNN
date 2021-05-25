# Corona GUI 


# https://github.com/Diwas524/corona-detection-model/ for trained model weights

Corona virus caused cluster of pneumonia cases, in late 2019,  majority 
suffering from only mild, cold-like symptoms.  According to researchers, the 
lining of the respiratory tree becomes injured, causing inflammation. This in 
turn irritates the nerves in the lining of the airway. Just a speck of dust can
stimulate a cough. If the condition becomes intense, lungs that become filled 
with inflammatory material become unable to get enough oxygen to the
bloodstream, reducing the body’s ability to take on oxygen and get rid of
carbon dioxide which finally lead to death.


The CNN consist layer of neurons and it is optimized for two-dimensional pattern
recognition. CNN has three types of layer namely convolutional layer, pooling 
layer and fully connected layer. Our network consists of 11 layers excluding the
input layer. The input layer takes in a RGB color image where each color channel
is processed separately.

The first 6 layers of convolution network are convolution layer. First 2
convolution layer applies 16 of 3*3 filters to an image in the layer. The other 
two layer applies 32 of 3*3 filters to an image. And the last 2 layers of
convolution applies 64 of 3*3 filters to an image. The nonlinear transformation 
sublayer employs the ReLU activation function. The max pooling sublayer applies 
a 2*2 filter to the image which results in reducing the image size to its half. 
At this point, convolution network extracts 64 features, each represented by a 
32*32 array for each color channel.
