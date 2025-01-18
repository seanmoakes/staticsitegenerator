import os
from markdown_blocks import (
    markdown_to_html_node,
)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("Invalid markdown: no h1 found")


def generate_page(from_path, template_path, dest_path):
    # Print message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read files
    markdown = read_file_contents(from_path)
    template = read_file_contents(template_path)

    # convert markdown to HTML string

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    # Get title
    title = extract_title(markdown)

    # Replace {{ Title }} and {{ Content }}
    # placeholders in the template string
    print(template)
    print("\nReplacing Title and Content\n")
    generated = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    print(generated)

    # Write html page to dest_path
    with open(dest_path, "w") as f:
        f.write(generated)
        f.close()


def read_file_contents(file_path):
    contents = ""
    if os.path.isfile(file_path):
        f = open(file_path, "r")
        contents = f.read()
        f.close()
    else:
        raise FileNotFoundError(f"No file found at {file_path}")
    return contents
