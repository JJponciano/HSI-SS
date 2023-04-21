import os
from PIL import Image
import argparse

def apply_mask_to_image(image, mask, color, transparency=0.25):
    # Convert the mask to an RGBA image with the specified color
    colored_mask = Image.new("RGBA", mask.size, color)

    # Set the alpha channel of the colored mask based on the mask's intensity and transparency factor
    mask_pixels = mask.load()
    colored_mask_pixels = colored_mask.load()

    width, height = mask.size

    for y in range(height):
        for x in range(width):
            intensity = mask_pixels[x, y]
            alpha = int(intensity * transparency)
            colored_mask_pixels[x, y] = (colored_mask_pixels[x, y][0], colored_mask_pixels[x, y][1], colored_mask_pixels[x, y][2], alpha)

    # Combine the image with the colored mask
    return Image.alpha_composite(image, colored_mask)

def apply_masks_to_image(image_path, masks_directory, output_path):
    # Load the RGB image and convert it to an RGBA image
    image = Image.open(image_path).convert("RGBA")

    # Get a list of all the mask files in the directory and sort them alphabetically
    mask_files = sorted([f for f in os.listdir(masks_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    # Define a list of colors for each mask with adjusted transparency
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255),
        (255, 255, 0), (255, 0, 255), (0, 255, 255),
        (128, 0, 0), (0, 128, 0), (0, 0, 128),
        (128, 128, 0), (128, 0, 128), (0, 128, 128),
        (192, 0, 0), (0, 192, 0), (0, 0, 192),
        (192, 192, 0), (192, 0, 192), (0, 192, 192),
        (64, 64, 64), (128, 128, 128)
    ]

    # Apply each mask to the image with a corresponding color
    for mask_file, color in zip(mask_files, colors):
        mask_path = os.path.join(masks_directory, mask_file)
        mask = Image.open(mask_path).convert("L")  # Convert the mask to grayscale
        mask = mask.resize(image.size, Image.ANTIALIAS)  # Resize the mask to match the image dimensions
        image = apply_mask_to_image(image, mask, color)

    # Save the combined masked image to the output path
    image.save(output_path)
    return output_path

# Example usage: python my_script.py --image_path /path/to/image.png --masks_directory /path/to/masks/ --output_directory /path/to/output/mask.png
if __name__ == '__main__':
   # create an argument parser
    parser = argparse.ArgumentParser()

    # add arguments for image_path, masks_directory and output_directory
    parser.add_argument('--image_path', type=str, required=True, help='path to the input image file')
    parser.add_argument('--masks_directory', type=str, required=True, help='directory containing the annotation/mask files')
    parser.add_argument('--output_directory', type=str, required=True, help='directory to save the output mask file')

    # parse the arguments
    args = parser.parse_args()

    # access the file paths from the parsed arguments
    image_path = args.image_path
    masks_directory = args.masks_directory
    output_directory = args.output_directory

    output_path= apply_masks_to_image(image_path, masks_directory, output_directory)
    # Load and display the final masked image
    final_image = Image.open(output_path)
    final_image.show()
