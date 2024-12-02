from PIL import Image,ImageOps
import sys
import os
# implement a program that expects exactly two command-line arguments:
def main():
    if len(sys.argv) != 3:
        sys.exit("Wrong parameters")
    input_photo, output_photo = sys.argv[1],sys.argv[2]
    condition_checks(input_photo,output_photo)
    image_processor(input_photo, output_photo)

# The program should instead exit via sys.exit:
def condition_checks(input_photo,output_photo):
    # if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    try:
        fn_input, fext_input = os.path.splitext(input_photo)
        fn_output, fext_output = os.path.splitext(output_photo)
        extensions = [".jpg",".jpeg",".png"]
        if fext_input not in extensions:
            sys.exit("Wrong Input Extensions")
        if fext_output not in extensions:
            sys.exit("Wrong Output Extensions")
    # if the input’s name does not have the same extension as the output’s name
        if fext_input != fext_output:
            sys.exit("Input and output file extensions are not the same")
    # if the specified input does not exist.
    except(FileNotFoundError):
        sys.exit("File not FOUND")


# The program should then overlay shirt.png (which has a transparent background)
def image_processor(input_photo,output_photo):
    try:
        shirt = Image.open("shirt.png")
        photo1 = Image.open(input_photo)
        size = shirt.size
        photo1 = ImageOps.fit(photo1,size)
        photo1.paste(shirt,shirt)
        photo1.save(output_photo)
    except(FileNotFoundError,ValueError):
        sys.exit("File Not found ")

if __name__ == "__main__":
    main()