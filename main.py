import cv2
import os
from pathlib import Path

def find_the_image(file_name, directory_name):
    files_found = []
    for path, subdirs, files in os.walk(directory_name):
        for name in files:
            if file_name == name:
                file_path = os.path.join(path, name)
                files_found.append(file_path)

    if not files_found:
        print(f"No matching file '{file_name}' found in the specified directory.")
        return None

    print(files_found[0])
    return files_found[0]

image_name = input("Please enter the name of the image file that you want to process: ")
image_directory = input("Please enter the directory that may contain the image: ")

while True:
    image_path = Path(find_the_image(image_name, image_directory))

    if image_path is not None:
        new_working_directory = image_path.parent
        os.chdir(new_working_directory)

        color_image = cv2.imread(str(image_path))

        cartoon_style_selection = input("This script currently has 5 styles. Please type 1, 2, 3, 4 or 5. Type 6 to exit: ")

        if cartoon_style_selection == "1":
            gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 20)
            color_cartoon = cv2.bilateralFilter(color_image, 9, 300, 300)
            cartoon_image_style_1 = cv2.bitwise_and(color_cartoon, color_cartoon, mask=edges)
            cv2.imshow('cartoon_1', cartoon_image_style_1)
            cv2.waitKey()
            cv2.destroyAllWindows()

        elif cartoon_style_selection == "2":
            gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 20)
            color_enhanced = cv2.detailEnhance(color_image, sigma_s=10, sigma_r=0.15)
            cartoon_image_style_2 = cv2.bitwise_and(color_enhanced, color_enhanced, mask=edges)
            cv2.imshow('cartoon_2', cartoon_image_style_2)
            cv2.waitKey()
            cv2.destroyAllWindows()

        elif cartoon_style_selection == "3":
            gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 20)
            quantized = cv2.convertScaleAbs(cv2.detailEnhance(color_image, sigma_s=10, sigma_r=0.15))
            pencil_sketch = cv2.divide(gray, 255, scale=256)
            pencil_sketch = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2BGR)
            pencil_sketch = cv2.bitwise_and(pencil_sketch, quantized)
            cartoon_image_style_3 = cv2.bitwise_and(quantized, quantized, mask=edges)
            cv2.imshow('cartoon_3', cartoon_image_style_3)
            cv2.waitKey()
            cv2.destroyAllWindows()

        elif cartoon_style_selection == "4":
            bilateral_filter_d = 9
            bilateral_filter_sigma_color = 75
            bilateral_filter_sigma_space = 75
            bilateral_filtered_image = cv2.bilateralFilter(color_image, bilateral_filter_d,
                                                           bilateral_filter_sigma_color, bilateral_filter_sigma_space)
            edge_preserving_filtered_image = cv2.detailEnhance(bilateral_filtered_image, sigma_s=10, sigma_r=0.15)
            cv2.imshow('cartoon_4', edge_preserving_filtered_image)
            cv2.waitKey()
            cv2.destroyAllWindows()

        elif cartoon_style_selection == "5":
            upscaled_image = cv2.resize(color_image, None, fx=1, fy=1, interpolation=cv2.INTER_LANCZOS4)
            cv2.imshow('upscaled_image', upscaled_image)
            cv2.waitKey()
            cv2.destroyAllWindows()

        elif cartoon_style_selection == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid style selection. Please enter 1, 2, 3, 4, 5, or 6 to exit.")
    else:
        break
