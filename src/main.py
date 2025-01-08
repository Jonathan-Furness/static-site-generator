from generate.copy_files import copy_files_to_destination
from generate.generate_page import generate_pages_recursive


def main():

    copy_files_to_destination("./static", "./public")
    generate_pages_recursive("./src/content", "./template.html", "./public")


if __name__ == "__main__":
    main()
