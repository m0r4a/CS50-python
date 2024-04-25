def main():

    file_name = input("File name: ")

    clean_file_name = file_name.strip().lower()

# I did not want to add topics that have not been covered in the course yet
# but this was the closest to what has been taught in the course that I could think of.
    try:
        file_extension = clean_file_name.split(".").pop(-1)
    except IndexError:
        file_extension = "none"

    match file_extension:
        case "gif" | "png":
            print("image/", file_extension, sep='')

        case "jpg" | "jpeg":
            print("image/jpeg", sep='')

        case "pdf" | "zip":
            print("application/", file_extension, sep='')

        case "txt":
            print("text/plain")

        case _:
            print("application/octet-stream")


main()
