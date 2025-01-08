import os

from converters.markdown_to_html import markdown_to_html_node
from generate.extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str):

    print(f"GENERATING PAGE from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as from_file:
        markdown = from_file.read()

    with open(template_path) as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)

    with open(dest_path, "w") as dest_file:
        dest_file.write(html_page)


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
):

    dirs = os.listdir(dir_path_content)

    for directory in dirs:
        path = os.path.join(dir_path_content, directory)
        if os.path.isfile(path):
            file_name = directory.strip(".md")
            dest_path = os.path.join(dest_dir_path, f"{file_name}.html")
            generate_page(path, template_path, dest_path)
        else:
            dest_path = os.path.join(dest_dir_path, directory)
            generate_pages_recursive(path, template_path, dest_path)
