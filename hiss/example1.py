import os.path

import cv2
from SemanticSegmentation import *
import matplotlib.pyplot as plt

if __name__ == '__main__':
    train_dir_img = "C:\\Users\\49151\\Documents\\2023\\i3mainz\\data\\dataset1\\images\\training"
    train_dir_annotations = "C:\\Users\\49151\\Documents\\2023\\i3mainz\\data\\dataset1\\annotations\\training"
    inp_dir = "C:\\Users\\49151\\Documents\\2023\\i3mainz\\data\\dataset1\\images\\validation"
    annotations_dir = "C:\\Users\\49151\\Documents\\2023\\i3mainz\\data\\dataset1\\annotations\\validation"
    out_dir = "C:\\Users\\49151\\Documents\\2023\\i3mainz\\data\\dataset1\\outputs"

    num_classes = 51
    channel = 3
    epochs = 40
    input_size=192*2
    input_height = input_size
    input_width = input_size

    ss=SemanticSegmentation(num_classes=num_classes,channel=channel,epochs=epochs,input_width=input_width,input_height=input_height)
    if os.path.isfile(ss.path):
        print("Load from file ",ss.path)
        ss.load(ss.path)
    else:
        print("trained ->",ss.train(train_dir_img=train_dir_img,train_dir_annotations=train_dir_annotations))
    print(ss.evaluation(inp_dir,annotations_dir))
    ss.prediction(inp_dir,out_dir)

    # get a list of all files in the directory
    files = os.listdir(inp_dir)
    for f in files:
        # Create a figure with two subplots
        fig, axs = plt.subplots(1, 3)

        # Plot the first array in the left subplot
        orig = cv2.imread(os.path.join(inp_dir, f), cv2.IMREAD_UNCHANGED)
        axs[0].imshow(orig)
        axs[0].set_title(f)

        gt = cv2.imread(os.path.join(annotations_dir, f), cv2.IMREAD_UNCHANGED)
        axs[1].imshow(gt)
        axs[1].set_title('Ground truth')

        result = cv2.imread(os.path.join(out_dir, f), cv2.IMREAD_UNCHANGED)
        axs[2].imshow(result)
        axs[2].set_title('Results')
        plt.show()


