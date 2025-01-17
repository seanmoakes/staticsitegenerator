import os
import shutil


def copy_src_contents(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(source_dir):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(dest_dir, filename)
        print(f" * {src_path} -> {dst_path}")

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_src_contents(src_path, dst_path)
    print(f"Finished copying contents of {source_dir} to {dest_dir}.")
