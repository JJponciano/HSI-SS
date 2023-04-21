#
# import argparse
#
# if __name__ == '__main__':
#     # Set up the command-line argument parser
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-input", type=str, help="Path to the YAML config file")
#
#     # Parse the command-line arguments
#     args = parser.parse_args()
#     if not args.config:
#         config_path = input("Please enter the path to the config file: ")
#     else:
#         config_path = args.config
#     # get a list of all files in the directory
#     files = os.listdir(input_dir)
#     for f in files:
#         # Create a figure with two subplots
#         fig, axs = plt.subplots(1, 2)
#
#         # Plot the first array in the left subplot
#         orig = cv2.imread(os.path.join(input_dir, f), cv2.IMREAD_UNCHANGED)
#         axs[0].imshow(orig)
#         axs[0].set_title(f)
#
#         result = cv2.imread(os.path.join(output_dir, f), cv2.IMREAD_UNCHANGED)
#         axs[1].imshow(result)
#         axs[1].set_title('Prediction')
#         plt.show()