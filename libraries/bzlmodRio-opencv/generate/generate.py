import os
from get_opencv_dependencies import get_opencv_dependencies

from bazelrio_gentool.generate_group import generate_group
from bazelrio_gentool.generate_module_project_files import (
    generate_module_project_files,
    create_default_mandatory_settings,
)
from bazelrio_gentool.clean_existing_version import clean_existing_version
from bazelrio_gentool.cli import add_generic_cli, GenericCliArgs
import argparse
import subprocess


def main():
    SCRIPT_DIR = os.environ["BUILD_WORKSPACE_DIRECTORY"]
    REPO_DIR = os.path.join(SCRIPT_DIR, "..", "..", "..", "..", "libraries", "bzlmodRio-opencv")
    output_dir = os.path.join(REPO_DIR, "libraries")

    parser = argparse.ArgumentParser()
    add_generic_cli(parser)
    args = parser.parse_args()

    group = get_opencv_dependencies()

    mandatory_dependencies = create_default_mandatory_settings(GenericCliArgs(args))

    clean_existing_version(REPO_DIR)
    generate_module_project_files(REPO_DIR, group, mandatory_dependencies)
    generate_group(output_dir, group, force_tests=args.force_tests)

    buildifier_args = ["/home/pjreiniger/go/bin/buildifier", "--lint=fix", "-warnings", "all", "-r", REPO_DIR]
    subprocess.check_call(buildifier_args)


if __name__ == "__main__":
    """
    bazel run //:generate && buildifier --lint=fix -r ..
    """
    main()
