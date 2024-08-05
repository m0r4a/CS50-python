from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        self.cell(0, 30, "CS50 Shirtificate", align='C')


def main():
    image_width = 180
    image_height = 200
    name = input("Name: ") + " took CS50"

    # Getting the center of the image
    x_center, y_center = get_center(image_width, image_height)

    # Creating the instance
    pdf = PDF(orientation="P", unit="mm", format="A4")

    # Adding a page
    pdf.add_page()

    # Setting the shirt image
    pdf.image("shirtificate.png", x_center, y_center, image_width)

    # Setting the user's name in the shirt
    pdf.set_font("helvetica", "", 25)
    pdf.set_text_color(255, 255, 255)

    # Calculate the position for the name
    y_name = y_center + 60

    # Add the name to the PDF
    pdf.set_xy(0, y_name)
    pdf.cell(210, 10, name, align='C')

    # Saving/outputting the file
    pdf.output("shirtificate.pdf")


def get_center(image_width: int, image_height: int):
    return ((210 - image_width) / 2, (297 - image_height) / 2)


if __name__ == "__main__":
    main()
