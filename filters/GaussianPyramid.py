#Set the finest scale layer to the image
#For each layer, going from next to finest to coarsest
#Obtain this layer by smoothing the next finest
#layer with a Gaussian, and then subsampling it end