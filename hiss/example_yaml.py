import csv
import os.path

import cv2
from SemanticSegmentation import *
import matplotlib.pyplot as plt
import yaml
import argparse

if __name__ == '__main__':
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-config", type=str, help="Path to the YAML config file")

    # Parse the command-line arguments
    args = parser.parse_args()

    # If config path is not specified, ask user to enter it
    if not args.config:
        config_path = input("Please enter the path to the config file: ")
    else:
        config_path = args.config
    # Check if evaluation and evaluation_annotations directories exist in config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    num_classes = config['model'].get('num_classes', '')
    channel =config['model'].get('channel', '')
    epochs = config['model'].get('epochs', '')
    weights =config['model'].get('weights', '')
    input_image_height=config['model'].get('input_image_height', '')
    input_image_width= config['model'].get('input_image_width', '')
    training= config['dataset'].get('training', '')
    annotations= config['dataset'].get('annotations', '')


    ss=SemanticSegmentation(num_classes=num_classes,channel=channel,epochs=epochs,input_width=input_image_width,input_height=input_image_height)

    if config and config.get('dataset'):
        print(":: Training:")
        if os.path.isfile(weights):
            print("Weights loaded from: ",weights)
            ss.load(weights)
        else:
            ss.train(train_dir_img=training,train_dir_annotations=annotations,path=weights)
            print("Trained model saved: ",weights)

        print(":: Evaluation:")

        eval_dir = config['dataset'].get('evaluation', '')
        eval_ann_dir = config['dataset'].get('evaluation_annotations', '')
        eval_out_dir= config['dataset'].get('evaluation_output', '')
        if eval_dir and os.path.isdir(eval_dir) and eval_ann_dir and os.path.isdir(eval_ann_dir)and eval_out_dir and os.path.isdir(eval_out_dir):
            evaluation = ss.evaluation(eval_dir, eval_ann_dir)
            # Save the evaluation in the output folder
            # Open a CSV file for writing
            with open(os.path.join(eval_out_dir,'evaluation.csv'), mode='w') as csv_file:

                # Create a CSV writer object
                fieldnames = list(evaluation.keys())
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                # Write the header row
                writer.writeheader()

                # Write the data rows
                writer.writerow(evaluation)

        else:
            print("One or all of the directories do not exist.")


        print(":: Inference:")
        # Check if evaluation and evaluation_annotations directories exist in config
        if config and config.get('dataset'):
            input_dir = config['dataset'].get('input', '')
            output_dir = config['dataset'].get('output', '')
            if input_dir and os.path.isdir(input_dir) and output_dir and os.path.isdir(output_dir):
                print("Inference...")
                ss.prediction(input_dir, output_dir)
                print("Done!")
            else:
                print("One or both of the directories (input and output) do not exist.")
        else:
            print("Config or dataset is not defined. Evaluation is ignored!")
    else:
        print("Config or dataset is not defined!")




