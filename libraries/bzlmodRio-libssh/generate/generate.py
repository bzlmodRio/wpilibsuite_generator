import argparse
import os

from bazelrio_gentool.clean_existing_version import clean_existing_version
from bazelrio_gentool.cli import GenericCliArgs, add_generic_cli
from bazelrio_gentool.generate_group import generate_group
from bazelrio_gentool.generate_module_project_files import (
    create_default_mandatory_settings,
    generate_module_project_files,
)
from get_libssh_dependencies import get_libssh_dependencies


def main():
    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]
    REPO_DIR = os.path.join(SCRIPT_DIR, "..")
    output_dir = os.path.join(REPO_DIR, "libraries")

    parser = argparse.ArgumentParser()
    add_generic_cli(parser)
    args = parser.parse_args()

    group = get_libssh_dependencies()

    mandatory_dependencies = create_default_mandatory_settings(GenericCliArgs(args))

    clean_existing_version(REPO_DIR)
    generate_module_project_files(
        REPO_DIR,
        group,
        mandatory_dependencies,
        test_macos=False,
    )
    generate_group(output_dir, group, force_tests=args.force_tests)


if __name__ == "__main__":
    """
    bazel run //:generate && buildifier --lint=fix -r ..
    """
    main()
