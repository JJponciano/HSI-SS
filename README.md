# HSI-SS: Python Deep Learning API for Semantic Segmentation in Hyperspectral Images and Traditional Images

## Information
HSI-SS is a Python API based on deep learning approach that provides state-of-the-art algorithms for semantic segmentation in hyperspectral images, while also supporting traditional images. The package includes a models such as UNet, and PSPNet that can be trained and tested on your own data. The package also includes data loaders, preprocessing utilities, and evaluation metrics to streamline the training and testing process. HSI-SS is designed for data scientists, researchers, and practitioners working in the field of hyperspectral imaging, remote sensing, and computer vision. With HSI-SS, you can quickly and easily develop accurate semantic segmentation models for hyperspectral and traditional images, and use them to solve a variety of real-world problems.
HSI-SS is built on top of the popular image-segmentation-keras repository, which provides a strong foundation for developing and testing image segmentation models in Keras. By leveraging the pre-built models, utilities, and codebase of image-segmentation-keras, HSI-SS is able to deliver a powerful and easy-to-use package for semantic segmentation in hyperspectral and traditional images

## Dataset Directory Structure

This directory structure is designed to organize data for deep learning projects.

### Directory Structure

The following directory structure is recommended for a dataset:
```
dataset/
├── training/
│ ├── data/
│ └── annotations/
├── eval/
│ ├── data/
│ ├── annotations/
│ └── output/
├── inputs/
└── outputs/
```
- `dataset/`: The root directory for the dataset.
- `training/`: The directory containing the training data and annotations.
- `training/data/`: The directory containing the training data.
- `training/annotations/`: The directory containing the annotations for the training data.
- `eval/`: The directory containing the evaluation data, annotations, and output.
- `eval/data/`: The directory containing the evaluation data.
- `eval/annotations/`: The directory containing the annotations for the evaluation data.
- `eval/output/`: The directory for output files generated during evaluation.
- `inputs/`: The directory containing input files for inference.
- `outputs/`: The directory for output files generated during inference.

### Creating the Directory Structure

To create this directory structure, you can run the following `mkdir` commands:

```sh
mkdir -p dataset/training/data
mkdir -p dataset/training/annotations
mkdir -p dataset/eval/data
mkdir -p dataset/eval/annotations
mkdir -p dataset/eval/output
mkdir -p dataset/inputs
mkdir -p dataset/outputs
```
### Usage
To use this directory structure for your deep learning project, follow these steps:

1. Create a new directory for your dataset.
2. Within the dataset directory, create the following directories: `training/data`, `training/annotations`, `eval/data`, `eval/annotations`, `eval/output`, `inputs`, `outputs`.
3. Place your training data in `training/data`, and annotations in `training/annotations`.
4. Place your evaluation data in `eval/data`, and annotations in `eval/annotations`.
5. After running evaluation, output files will be saved in `eval/output`.
6. To perform inference, place input files in `inputs`, and the output files will be saved in `outputs`.

### Note:

- If you do not plan on performing evaluation or inference, you can omit the `eval/`, `inputs/`, and `outputs/` directories.
- If you have multiple datasets, you can create a similar directory structure for each dataset, and place them within a parent directory.
- Make sure that your training and evaluation data are stored in the appropriate directories, as the deep learning framework you are using may expect them to be in a certain location.
