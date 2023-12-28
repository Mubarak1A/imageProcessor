# JPG to PNG Converter

A simple Python script to convert all JPG files in a specified folder to PNG format and save them in a new folder.

## Usage

1. Ensure you have Python 3 installed on your system.
2. Open a terminal.
3. Clone the script repo on your manchine:
     ```git clone https://github.com/Mubarak1A/imageProcessor.git```
4. Navigate to the directory containing the script.
5. Run the script with the following command:

    ```bash
    python3 jpg_to_png_converter.py <Images_Folder> <Output_Folder>
    ```

   Replace `<Images_Folder>` with the path to the folder containing the JPG images you want to convert, and `<Output_Folder>` with the desired path for the output folder.

## Example

```bash
python3 jpg_to_png_converter.py input_images output_images
```

This will convert all JPG files in the `input_images` folder and save the PNG files in the `output_images` folder.

## Code Analysis

The script takes two command-line arguments - the path to the folder containing JPG images (`Images_Folder`) and the path to the desired output folder (`Output_Folder`).

1. It checks if the specified output folder exists; if not, it creates the folder.

2. For each file in the input folder, the script uses the [PIL (Pillow)](https://pillow.readthedocs.io/en/stable/) library to open the JPG image.

3. It extracts the filename without the extension and saves the image in PNG format with the same name in the output folder.

4. After each conversion, it prints a message indicating successful conversion.

## Requirements

- Python 3
- Pillow library (PIL)

Install Pillow using the following command:

```bash
pip install Pillow
```

Note: This script assumes that all files in the specified input folder are JPG images. Make sure to provide the correct folder paths for images and output accordingly.
