def main():

    file_name = input("File name: ")

    clean_file_name = file_name.strip().lower()

    if len(clean_file_name.split(".")) >= 2:
        file_extension = clean_file_name.split(".").pop(-1)

    else:
        file_extension = "None"

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
