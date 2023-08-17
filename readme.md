# Sea Animal Recognition

The project will take in an image of an sea animal and it can detect more than 20 different types of sea animals. It will help people detect what type of sea animal they saw when snorkeling in the ocean. 

![image of an jellyfish](https://i.imgur.com/sEnY0qg.jpg[/img])

## The Algorithm

This project is a resnet 50 model trained using this dataset with more than 20 different sea animals. When an image is provided to the model, the algorithm takes in the image and runs it through the model to determine what type of sea animal it is. 

## Training the model

1. Clone the jetson-inference project from GitHub using "git clone --recursive https://github.com/dusty-nv/jetson-inference"
2. Change directories to the jetson-inference directory
3. Download the python packages using "sudo apt-get install libpython3-dev python3-numpy"
4. Make a directory called build and run "cmake ../" in the build directory
5. Download this dataset: https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste
6. Make a file called labels.txt and put all the names of the different directories inside
7. Get into the docker by running './docker/run.sh'.
8. Change directories to the jetson-inference/python/training/classification
9. Train the model by running 'python3 train.py --arch=resnet50 --model-dir=models/sea_animals data/sea_animals_split'
10. Export to a onnx file with 'python3 onnx_export.py --model-dir=models/sea_animals'

## Running this project

1. Make sure you are out of the docker and is in the jetson-inference/python/training/classification directory
2. Make sure you have resnet50.onnx in sea_animals and labels.txt in the data on the Jetson Nano    
4. Make NET equal to the sea_animals resnet50.onnx is stored in; Make LABELS equal to the folder labels.txt is stored
5. To classify an image, replace image with the image you want to run through the model and output with what file you want output the image to in this code: "imagenet.py --model=$NET/resnet50.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt image output", then run the code. 
6. Open the output file to see the result. 

[View a video explanation here](video link)
