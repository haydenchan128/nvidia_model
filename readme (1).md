# Sea Animal Recognition

The project will take in an image of an sea animal and it can detect more than 20 different types of sea animals. It will help people detect what type of sea animal they saw when snorkeling in the ocean. 

![image of an sea animal](direct image link here)

## The Algorithm

This project is a resnet 50 model trained using this dataset https://www.kaggle.com/datasets/vencerlanz09/sea-animals-image-dataste. When an image is provided to the model, the algorithm takes in the image and runs it through the model to determine what type of sea animal it is. 

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 

## Running this project

1. Clone the jetson-inference project from GitHub using "git clone --recursive https://github.com/dusty-nv/jetson-inference"
2. Change directories to the jetson-inference directory
2. Download the python packages using "sudo apt-get install libpython3-dev python3-numpy"
3. Download resnet50.onnx and labels.txt from this project on to the Jetson Nano    
4. Make a directory called build and run "cmake ../" in the build directory
5. Navigate to the jetson-inference/python/training/classification directory
6. Make NET equal to the folder resnet50.onnx is stored in; Make LABELS equal to the folder labels.txt is stored;
7. To classify an image, replace IMAGE with the image you want to run through the model and OUTPUT with where you want to put the image in this code "imagenet.py --model=$NET/resnet50.onnx --input_blob=input_0 --output_blob=output_0 --labels=$LABELS/labels.txt IMAGE OUTPUT", then run the code. 
8. Open the output file on your computer to see the result. 


In my project, I used a sea_animal dataset and I have more than 20 different classes to detect the many different sea animals. Before I was able to use the dataset, I needed to used split_data.py to seperate the data between train test and val, so I can have some training data and testing data. 

I downloaded jetson-inference from Github onto my nano in order to make my project. I used the Resnet 50 model to train my project. 

To train the model, I needed to go 
python3 train.py --arch=resnet50 --model-dir=models/sea_animals2 data/sea_animals_split

NET=models/sea_animals2
DATASET=data/sea_animals_split

imagenet.py --model=$NET/resnet50.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/Shrimp/shrimp1.jpg shrimp.jpg

1. Add steps for running this project.
2. Make sure to include any required libraries that need to be installed for your project to run.

[View a video explanation here](video link)
