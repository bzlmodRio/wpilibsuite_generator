import os
import re

from bazelrio_gentool.auto_update_utils import get_latest_tag, split_tag


def main():
    latest_tag = get_latest_tag("wpilibsuite", "thirdparty-libssh")

    new_year, new_version = split_tag(latest_tag)

    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]

    file_to_replace = os.path.join(SCRIPT_DIR, "get_libssh_dependencies.py")

    with open(file_to_replace, "r") as f:
        contents = f.read()

    contents = re.sub('( +)year = "(.*)"', f'\\1year = "{new_year}"', contents)
    contents = re.sub(
        '( +)version = f?"(.*)"', f'\\1version = "{new_version}"', contents
    )

    with open(file_to_replace, "w") as f:
        f.write(contents)


if __name__ == "__main__":
    main()
