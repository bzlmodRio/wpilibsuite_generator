import os
import re
from bazelrio_gentool.auto_update_utils import download_url


def main():
    contents = download_url(
        "https://raw.githubusercontent.com/wpilibsuite/WPILibInstaller-Avalonia/main/scripts/versions.gradle"
    )

    for line in contents.decode("utf-8").split("\n"):
        search = re.search("ext.jdkVersion = '(.*)'", line)
        if search:
            version = search[1]

    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]

    file_to_replace = os.path.join(SCRIPT_DIR, "get_toolchain_dependencies.py")

    with open(file_to_replace, "r") as f:
        contents = f.read()
    contents = re.sub(
        '( +)jdk_version = "(.*)"', f'\\1jdk_version = "{version}"', contents
    )

    with open(file_to_replace, "w") as f:
        f.write(contents)
    print(version)


if __name__ == "__main__":
    main()
