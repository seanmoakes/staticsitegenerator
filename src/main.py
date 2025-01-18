# from textnode import TextNode, TextType
import os
import shutil
from copystatic import copy_src_contents
from generate_html import generate_pages_recursive

dir_src_static = "./static"
dir_dst_public = "./public"
dir_content = "./content"
file_template = "./template.html"
# file_dest = "./public/index.html"


def main():
    print(f"Deleting contents of {dir_dst_public}...")
    if os.path.exists(dir_dst_public):
        shutil.rmtree(dir_dst_public)

    print(f"Copying contents of {dir_src_static} to {dir_dst_public}")
    copy_src_contents(dir_src_static, dir_dst_public)
    generate_pages_recursive(dir_content, file_template, dir_dst_public)


main()
