import sys
from PIL import Image, ImageOps
from os.path import splitext


def main():
    case_insensitive_arguments = [arg.lower() for arg in sys.argv]
    input_image, output_image = check_arguments(case_insensitive_arguments)
    image_creator(input_image, output_image)


def check_arguments(arguments: list):
    valid_extensions = (".png", ".jpeg", ".jpg")

    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")

    elif len(arguments) < 3:
        sys.exit("Too few command-line arguments")

    _, input_file_extension = splitext(arguments[1])
    _, output_file_extension = splitext(arguments[2])

    if input_file_extension not in valid_extensions:
        sys.exit("Error: Input file not an image file")

    elif output_file_extension not in valid_extensions:
        sys.exit("Error: Output file not an image file")

    elif arguments[1].startswith("../"):
        sys.exit("Error: File not in current directory")

    elif input_file_extension != output_file_extension:
        sys.exit("Error: Input and output have different extensions")
    else:
        return arguments[1], arguments[2]


def image_creator(input_image, output_image):
    try:
        input_image = Image.open(input_image)
    except FileNotFoundError:
        sys.exit("Error: Input does not exist")

    shirt = Image.open("shirt.png")

    resized_image = ImageOps.fit(input_image, shirt.size)
    resized_image.paste(shirt, shirt)
    resized_image.save(output_image)


if __name__ == "__main__":
    main()
