import os
from pathlib import Path
from markdown_blocks import (
    markdown_to_html_node,
)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Invalid markdown: no h1 found")


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = read_file_contents(from_path)
    template = read_file_contents(template_path)
    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
        f.close()


def generate_pages_recursive(
    dir_path_content, template_path, dest_dir_path, basepath="/"
):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dst_path = os.path.join(dest_dir_path, filename)
        if not os.path.isfile(src_path):
            generate_pages_recursive(src_path, template_path, dst_path, basepath)
        elif Path(src_path).suffix == ".md":
            html_path = Path(dst_path).with_suffix(".html")
            generate_page(src_path, template_path, html_path, basepath)


def read_file_contents(file_path):
    contents = ""
    if os.path.isfile(file_path):
        f = open(file_path, "r")
        contents = f.read()
        f.close()
    else:
        raise FileNotFoundError(f"No file found at {file_path}")
    return contents
